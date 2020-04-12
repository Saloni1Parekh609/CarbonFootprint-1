from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=255, default="India")
    diet = models.CharField(max_length=255, default="Vegetarian")
    fuel = models.CharField(max_length=255, default="Petrol")
    scooter = models.BooleanField(default=True)
    family = models.IntegerField(null=True)
    electricity = models.CharField(max_length=255, default="One-Three")

    """footprint = models.FloatField(default=0)
    time = models.FloatField(default=0)
    meal = models.FloatField(default=0)
    journey_time = models.IntegerField(default=0)
    compost = models.IntegerField(default=0)
    solar = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    consumer_type = models.CharField(max_length=100, default="")
    consumer_number = models.IntegerField(default=0)
    bun = models.IntegerField(default=0)"""

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


"""
COUNTRY_FIELD = (
        (1, 'India'),
        (2, 'USA'),
        (3, 'UK'),
    )
    DIET_FIELD = (
        (1, 'Heavy_meat'),
        (2, 'Medium_meat'),
        (3, 'Low_meat'),
        (4, 'Pescatarians'),
        (5, 'Vegetarian'),
        (6, 'Vegan'),
    )
    FUEL = (
        ('die', 'Diesel'),
        ('pet', 'Petrol'),
        ('none', 'None'),
    )
    ELECTRICITY = (
        (1, 'one-two'),
        (3, 'three-five'),
        (6, 'six')
    )
    """