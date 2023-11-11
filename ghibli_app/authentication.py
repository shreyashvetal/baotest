import base64
import hashlib
from django.conf import settings
from ghibli_app.models import UserMerchant
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class GhibliKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Basic '):
            return None
        try:
            auth_data = base64.b64decode(auth_header[len('Basic '):]).decode('utf-8')
        except UnicodeDecodeError:
            return None

        expected_api_key = settings.API_KEY
        if f"{expected_api_key}:" in auth_data:
            salt = auth_data[len(f"{expected_api_key}:"):]

            try:
                generate_sha256_hash = hashlib.sha256(salt.encode('utf-8')).hexdigest()
                user_merchant = UserMerchant.objects.get(salt=generate_sha256_hash)
                request.user_merchant = user_merchant
                return (user_merchant, None)
            except UserMerchant.DoesNotExist:
                pass
            except Exception as e:
                print("An error occurred:", e)
        raise AuthenticationFailed('Invalid API key')
