import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import generics

class MovieList(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        # Check if cached data is available
        cached_data = cache.get('ghibli_movies')

        if cached_data:
            return Response(cached_data)

        # Fetch data from the Ghibli API
        response = requests.get(settings.GHIBLI_API_URL)

        if response.status_code == 200:
            movies = response.json()

            # Customize the response by adding 'actors' instead of 'people'
            for movie in movies:
                movie['actors'] = self.get_actors(movie.get('people', []))
                movie.pop('people', None)

            # Customize the response structure
            response_data = {
                'success': True,
                'data': movies,
            }

            # Cache the data for 1 minute
            cache.set('ghibli_movies', response_data, 60)

            return Response(response_data)

        return Response({'success': False, 'error': 'Unable to fetch movie data'})

    def get_actors(self, people_list):
        temp_list = []

        for people_url in people_list:
            try:
                response = requests.get(people_url)
                if response.status_code == 200:
                    data_list = response.json()
                    for data in data_list:
                        temp_dict = {
                            "id": data.get("id", ''),
                            "name": data.get("name", ''),
                            'species': data.get('species', ''),
                            'url': data.get('url', '')
                        }
                        temp_list.append(temp_dict)
            except requests.RequestException as e:
                pass

        return temp_list
