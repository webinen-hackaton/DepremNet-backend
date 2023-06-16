import dataclasses
from datetime import datetime
import jwt

from django.conf import settings

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

def create_token(user_id:int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.utcnow() + settings.JWT_EXP_DELTA,
        iat=datetime.utcnow()
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    return token