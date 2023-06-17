from django.conf import settings
from rest_framework import (
    authentication,
    exceptions
)
import jwt

from . import models

class CustomAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        try:
            token = request.headers.get("Authorization")
        except Exception:
            raise ValueError(f"Token error: {token}")

        if not token:
            return None
        
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        except Exception:
            raise exceptions.AuthenticalstionFailed("Unauthorized")
        
        user = models.User.objects.filter(id=payload["id"]).first()

        return (user, None)