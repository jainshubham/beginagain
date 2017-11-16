from django.db import models
from django.contrib.auth.models import User
from enum import unique, IntEnum
from profiles.utils import get_choices
from phonenumber_field.modelfields import PhoneNumberField
from django import forms


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


class Profile(models.Model):
    """ The basic matrimonial profile of a person on our app.

    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    birth_date_time = models.DateTimeField()
    place_of_birth = models.CharField(max_length=30)
    approved_by = models.ForeignKey(User)
    approved_on = models.DateTimeField()
    body_type = models.IntegerField(default=0, null=True, choices=get_choices(BodyType))
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    mother_tongue = models.CharField(max_length=30)
    religion = models.CharField(max_length=30)
    physical_status = models.IntegerField(default=0, null=True, choices=get_choices(AIS))
    caste = models.CharField(max_length=30)
    gothram = models.CharField(max_length=30)
    zodiac = models.CharField(max_length=30)
    star = models.CharField(max_length=30)
    eating_habit =  models.IntegerField(default=0, null=True, choices=get_choices(EatingHabit))
    drinking_habit = models.IntegerField(default=0, null=True, choices=get_choices(DrinkingHabit))
    smoking_habit = models.IntegerField(default=0, null=True, choices=get_choices(SmokingHabit))
    country =  models.CharField(max_length=30)
    city =  models.CharField(max_length=30)
    state =  models.CharField(max_length=30)
    pincode =  models.CharField(max_length=30)
    education =  models.CharField(max_length=30)
    contact_no = PhoneNumberField(blank=True)
    images = models.ImageField()
    about_me = models.CharField(max_length=500)
    require_details =  models.CharField(max_length=30)
    marital_status = models.IntegerField(default=0, null=True, choices=get_choices(MaritalStatus))
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    email_id = models.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    gender = models.IntegerField(default=0, null=True, choices=get_choices(Gender))
    # login_status = models.BooleanField(choices=LOGIN_STATUS) // Cant remember this
    #profile_status = models.BooleanField(choices=PROFILE_STATUS)
    #serving = models.BooleanField(choices=SERVING_STATUS)

