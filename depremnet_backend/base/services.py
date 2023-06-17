import jwt
from django.conf import settings
from rest_framework import exceptions

def parse_jwt_id(token:str) -> int:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        return (payload["id"])
    except Exception:
        raise exceptions.AuthenticalstionFailed("Unauthorized")