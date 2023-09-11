from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, name, password=None, **extra_fields):
        if not name:
            raise ValueError('The Name field must be set')

        # phone_number 값을 password로 사용
        extra_fields.setdefault('phone_number', password)

        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(name, password, **extra_fields)


class User(AbstractBaseUser):
    name = models.CharField(max_length=255, unique=True, default='')
    phone_number = models.CharField(max_length=20, unique=True, default='')
    password = models.CharField(max_length=20, default='')
    # Rest of the fields

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []
    q1 = models.CharField(max_length=20, default='')
    q2 = models.CharField(max_length=20, default='')
    q3 = models.CharField(max_length=20, default='')
    q4 = models.CharField(max_length=20, default='')
    q5 = models.CharField(max_length=10, default='')
    q6 = models.CharField(max_length=10, default='')
    q7 = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    name = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    q1 = models.CharField(max_length=20, default='')
    q2 = models.CharField(max_length=20, default='')
    q3 = models.CharField(max_length=20, default='')
    q4 = models.CharField(max_length=20, default='')
    q5 = models.CharField(max_length=10, default='')
    q6 = models.CharField(max_length=10, default='')
    q7 = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name