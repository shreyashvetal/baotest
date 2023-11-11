# Ghibli Project

The Ghibli Project is a Django project that utilizes Django REST Framework (DRF) to create an API endpoint for retrieving information about Ghibli movies. The API includes details about movies, and instead of 'people,' it includes information about 'actors' with 'id,' 'name,' 'species,' and 'URL.'

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
  - [Endpoints](#endpoints)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shreyashvetal/baotest.git

2. Navigate to the project directory:
  cd baotest

4. Install dependencies:
    pip install -r requirements.txt
5. Apply migrations:
  python manage.py migrate
6. Run the development server:
  python manage.py runserver
  The API should be accessible at http://127.0.0.1:8000/.

## Project Structure
The project follows the standard Django project structure. Key directories include:

ghibli_app: Django app containing views, models, and serializers.
ghibli_project: Django project settings and configurations.
tests: Directory for test files.
## API Documentation
For API documentation, refer to https://ghibli.rest/docs/.

### Endpoints
GET /api/movies/: Retrieve a list of movies with details.
Tests
Run tests using the following command:
  python manage.py test ghibli_app.tests
