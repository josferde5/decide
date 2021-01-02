from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.


class MyUserManager(BaseUserManager):
    def _create_user(self, username, email=None, sex=None, password=None, **extra_fields):

        if not username:
            raise ValueError('The given username must be set')

        user = self.model(
            username=self.model.normalize_username(username),
            email=MyUserManager.normalize_email(email),
            sex=sex,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, sex=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, sex, password, **extra_fields)

    def create_superuser(self, username, email, sex, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, sex, password, **extra_fields)


class UserProfile(AbstractUser):
    sex_types = (('M', 'Male'),
                 ('F', 'Female'))
    sex = models.CharField(max_length=1, choices=sex_types)

    REQUIRED_FIELDS = ['email', 'sex']

    objects = MyUserManager()

