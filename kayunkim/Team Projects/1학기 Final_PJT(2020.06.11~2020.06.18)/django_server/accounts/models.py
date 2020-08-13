from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password, date_of_birth, favorite_genre, email=None):
        print('create user')
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            favorite_genre=favorite_genre,
            username=username,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,         
            name=name,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, date_of_birth, favorite_genre, password, email=None):
        user = self.create_user(
            password=password,
            date_of_birth=date_of_birth,
            favorite_genre=favorite_genre,
            username=username,
            email=email,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    favorite_genre = models.CharField(max_length=100, null=True)
    
    REQUIRED_FIELDS = ['date_of_birth', 'favorite_genre']