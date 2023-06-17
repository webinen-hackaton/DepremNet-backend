from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)

class UserManager(BaseUserManager):

    def create_user(self, 
                    first_name:str, 
                    last_name:str, 
                    email:str,
                    phone_number:str,
                    nationality_id:str,
                    password:str=None, 
                    is_staff=False,
                    is_superuser=False) -> "User":
        if not email:
            raise ValueError("User mus have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not phone_number:
            raise ValueError("User must have a notionality id")
        if not nationality_id:
            raise ValueError("User must have a phone number")
        
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.nationality_id = nationality_id
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
    
    def create_staffuser(self, 
                         first_name:str, 
                         last_name:str, 
                         email:str, 
                         password:str,
                         phone_number:str,
                         nationality_id:str) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone_number=phone_number,
            nationality_id=nationality_id,
            is_staff=True,
        )
        user.save()

        return user

    def create_superuser(self, 
                         first_name:str, 
                         last_name:str, 
                         email:str, 
                         password:str,
                         phone_number:str,
                         nationality_id:str) -> "User":
       user = self.create_user(
           first_name=first_name,
           last_name=last_name,
           email=email,
           password=password,
           phone_number=phone_number,
           nationality_id=nationality_id,
           is_staff=True,
           is_superuser=True
       )
       user.save()

       return user
    
def user_directory_path(instance, filename):
    return 'media/user_{0}/{1}'.format(instance.id, filename)

class User(AbstractBaseUser):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    phone_number = models.CharField(max_length=12, unique=True)
    nationality_id = models.CharField(max_length=11, unique=True)
    is_staff = models.BooleanField(default=False)
    team = models.ForeignKey(
        'team.Team',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )
    location = models.ForeignKey(
        'base.Location',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None
    )
    username = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", "nationality_id"]

    def has_perm(self, perm, obj=None):
     return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self) -> str:
        return self.email