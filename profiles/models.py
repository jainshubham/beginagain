from django.db import models
from django.contrib.auth.models import User
from enum import unique, IntEnum
from profiles.utils import get_choices
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from django_measurement.models import MeasurementField
from measurement.measures import Weight, Distance
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import six, timezone
from datetime import datetime


@unique
class EatingHabit(IntEnum):
    VEGETARIAN = 1
    NON_VEGETARIAN = 2

@unique
class SmokingHabit(IntEnum):
    REGULAR = 1
    OCCASIONAL = 2
    NON_SMOKER = 0

@unique
class DrinkingHabit(IntEnum):
    REGULAR = 1
    OCCASIONAL = 2
    NON_DRINKER = 0


@unique
class BodyType(IntEnum):
    SLIM = 0
    AVERAGE = 1
    OVERWEIGHT = 2

@unique
class MaritalStatus(IntEnum):
    UNMARRIED = 0
    DIVORCED = 1
    WIDOWED = 2
    MARRIED = 3

@unique
class Gender(IntEnum):
    MALE = 0
    FEMALE = 1
    OTHER = 2


@unique
class PROFILE_STATUS(IntEnum):
    ACTIVE = 0
    INACTIVE = 1

@unique
class AIS(IntEnum):
    MINOR = 1
    MODERATE = 2
    SERIOUS = 3
    SEVERE = 4
    CRITICAL = 5
    MAXIMAL = 6

@unique
class SERVING_STATUS(IntEnum):
    SERVING = 0
    NON_SERVING = 1


@unique
class HEIGHT_UNITS(IntEnum):
    INCH = 0
    CM = 1

class ProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    """ The basic matrimonial profile of a person on our app.

    """
    gender = models.IntegerField(default=0, null=True, choices=get_choices(Gender))
    age = models.PositiveIntegerField(null=True)
    serving = models.BooleanField(choices=get_choices(SERVING_STATUS), default=0)
    # has to be activated by admin only.
    approved_on = models.DateTimeField(default=timezone.now)
    birth_date_time = models.DateTimeField(null=True)
    place_of_birth = models.CharField(max_length=30, null=True)
    body_type = models.IntegerField(default=0, null=True, choices=get_choices(BodyType))
    height = MeasurementField(measurement=Distance, unit_choices=('mc'), null=True)
    weight = MeasurementField(measurement=Weight, null=True)
    mother_tongue = models.CharField(max_length=30, null=True)
    religion = models.CharField(max_length=30, null=True)
    physical_status = models.IntegerField(default=0, null=True, choices=get_choices(AIS))
    caste = models.CharField(max_length=30, null=True)
    gothram = models.CharField(max_length=30, null=True)
    zodiac = models.CharField(max_length=30, null=True)
    star = models.CharField(max_length=30, null=True)
    eating_habit =  models.IntegerField(default=0, null=True, choices=get_choices(EatingHabit))
    drinking_habit = models.IntegerField(default=0, null=True, choices=get_choices(DrinkingHabit))
    smoking_habit = models.IntegerField(default=0, null=True, choices=get_choices(SmokingHabit))
    country =  models.CharField(max_length=30, null=True)
    city =  models.CharField(max_length=30, null=True)
    state =  models.CharField(max_length=30, null=True)
    pincode =  models.CharField(max_length=30,null=True)
    education =  models.CharField(max_length=30, null=True)
    contact_no = PhoneNumberField(blank=True)
    images = models.ImageField(null=True)
    about_me = models.CharField(max_length=500, null=True)
    require_details =  models.CharField(max_length=30, null=True)
    marital_status = models.IntegerField(default=0, null=True, choices=get_choices(MaritalStatus))
    username = models.CharField(
        max_length=150,
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True, unique=True)
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    date_joined = models.DateTimeField(default=timezone.now)
    objects = ProfileManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


