import dataclasses
from datetime import datetime
import jwt

from django.conf import settings
from rest_framework import exceptions

from . import models

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import User

@dataclasses.dataclass
class UserDataClass:
    first_name:str
    last_name:str
    email:str
    phone_number:str
    nationality_id:str
    password:str = None
    id:int = None

    @classmethod
    def from_instance(cls, user:"User") -> "UserDataClass":
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone_number=user.phone_number,
            nationality_id=user.nationality_id,
            id=user.id,
        )
    
def create_user(user_dc: "UserDataClass"):
    instance = models.User(
        first_name=user_dc.first_name,
        last_name=user_dc.last_name,
        email=user_dc.email,
        phone_number=user_dc.phone_number,
        nationality_id=user_dc.nationality_id
    )

    if user_dc.password is not None:
        instance.set_password(raw_password=user_dc.password)
    
    instance.save()

    return UserDataClass.from_instance(instance)

def user_email_selector(email:str) -> "User":
    user = models.User.objects.filter(email=email).first()
    return user

def user_id_selector(id:int) -> "User":
    user = models.User.objects.filter(id=id).first()
    return user

def update_user(user_dc: "UserDataClass") -> "User":
    user = user_id_selector(user_dc.id)
    if user.email != user_dc.email:
        raise ValueError("email should be users' email")
    
    user.first_name = user_dc.first_name
    user.last_name = user_dc.last_name
    user.phone_number = user_dc.phone_number

    user.save()

def create_token(user_id:int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.utcnow() + settings.JWT_EXP_DELTA,
        iat=datetime.utcnow()
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    return token

def parse_jwt_id(token:str) -> int:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        return (payload["id"])
    except Exception:
        raise exceptions.AuthenticalstionFailed("Unauthorized")

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)