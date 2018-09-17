import logging

logger = logging.getLogger(__name__)

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def get_by_natural_key(self, email_):
        return self.get(**{self.model.USERNAME_FIELD: email_})

    def create_user(self, email, first_name, last_name, phone, age, password=None):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            age=age
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, password, age, phone):
        user = self.create_user(
            email,
            first_name,
            last_name,
            password,
            age,
            phone

        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, age, phone):
        user = self.create_user(
            email,
            first_name,
            last_name,
            password,
            age,
            phone
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class AppUser(AbstractBaseUser):
    username = None
    email = models.EmailField(('email'), unique=True)
    first_name = models.CharField(('first_name'), max_length=100)
    last_name = models.CharField(('last_name'), max_length=100)
    phone = models.CharField(('phone'), max_length=10, blank=True, null=True)
    age = models.CharField(('age'), max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'age']

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return  self.email

    def has_perms(self, perm, ob=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def natural_key(self):
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    objects = UserManager()
