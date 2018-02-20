from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

from enum import unique, IntEnum
from phonenumber_field.modelfields import PhoneNumberField
from django_measurement.models import MeasurementField
from measurement.measures import Weight, Distance
from datetime import datetime, timedelta

from profiles.utils import get_choices

"""
TODO: Django Cities, counties, state, mother tongue, cast gotra star, Zodiac Religion
TODO: Register
TODO: Add docs. 


"""


@unique
class EatingHabit(IntEnum):
    VEGETARIAN = 0
    NON_VEGETARIAN = 1


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
class ProfileStatus(IntEnum):
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
class ServingStatus(IntEnum):
    SERVING = 0
    NON_SERVING = 1


@unique
class HeightUnits(IntEnum):
    INCH = 0
    CM = 1


class ProfileManager(BaseUserManager):
    """ The class that manages the admin forms for class Prrofile

    """
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
    gender = models.IntegerField(default=0, null=False, choices=get_choices(Gender))
    age = models.PositiveIntegerField(null=True, default=18)
    is_serving = models.BooleanField(choices=get_choices(ServingStatus), default=0)
    approved_on = models.DateTimeField(default=timezone.now)
    birth_date_time = models.DateTimeField(default=datetime.now()-timedelta(366*18))
    place_of_birth = models.CharField(max_length=30, blank=True)
    body_type = models.IntegerField(default=0, choices=get_choices(BodyType))
    height = MeasurementField(measurement=Distance, unit_choices='mc', default=100)
    weight = MeasurementField(measurement=Weight, default=60)
    mother_tongue = models.CharField(max_length=30, blank=True)
    religion = models.CharField(max_length=30, blank=True)
    physical_status = models.IntegerField(default=3, choices=get_choices(AIS))
    caste = models.CharField(max_length=30, blank=True)
    gothram = models.CharField(max_length=30, blank=True)
    zodiac = models.CharField(max_length=30, blank=True)
    star = models.CharField(max_length=30, blank=True)
    eating_habit = models.IntegerField(default=0, choices=get_choices(EatingHabit))
    drinking_habit = models.IntegerField(default=0, choices=get_choices(DrinkingHabit))
    smoking_habit = models.IntegerField(default=0, choices=get_choices(SmokingHabit))
    country = models.CharField(max_length=30, default='Indian', blank=True)
    city = models.CharField(max_length=30,  blank=True)
    state = models.CharField(max_length=30,  blank=True)
    pincode = models.CharField(max_length=30,  blank=True)
    education = models.CharField(max_length=30,  blank=True)
    contact_no = PhoneNumberField(blank=True)
    images = models.ImageField(null=True, upload_to="profile_pictures")
    about_me = models.CharField(max_length=500,  blank=True)
    require_details = models.CharField(max_length=30,  blank=True)
    marital_status = models.IntegerField(default=0, choices=get_choices(MaritalStatus))
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    interest_shown = models.ManyToManyField('self', related_name='interest_received')
    matches = models.ManyToManyField('self', related_name='matches')
    objects = ProfileManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name']

    def save(self, *args, **kwargs):
        # if self.gender == 1 and self.images == "profile_pictures/male.jpeg":
        #     self.images = "profile_pictures/female.jpeg"
        # else:
        #     self.images = "profile_pictures/male.jpeg"
        super(Profile, self).save(*args, **kwargs)


    def get_full_name(self):
        """ The user is identified by their email address

        :return:
        """
        return self.email

    def get_short_name(self):
        """ The user is identified by their email address

        :return:
        """
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        """ Does the user have a specific permission?

        Simplest possible answer: Yes, always

        :param perm:
        :param obj:
        :return: True
        """
        return True

    def has_module_perms(self, app_label):
        """ Does the user have permissions to view the app `app_label`?
        # Simplest possible answer: Yes, always

        :param app_label:
        :return:
        """

        return True

    @classmethod
    def get_choices(cls):
        # get all members of the class
        choices = {}
        for key in Profile._meta.get_fields():
            try:
                choices[key.name] = key.choices
            except AttributeError:
                pass
        return choices

