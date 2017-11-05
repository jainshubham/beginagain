from django.db import models
from django.contrib.auth.models import User
from enum import unique, IntEnum, Enum
from profiles.utils import get_choices
from phonenumber_field.modelfields import PhoneNumberField

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

class Profile(models.Model):
    """

    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    approved_by = models.ForeignKey(User)
    approved_on = models.DateTimeField()
    body_type = models.IntegerField(default=0, null=True, choices=get_choices(BodyType))
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    mother_tongue = models.CharField(max_length=30)
    religion = models.CharField(max_length=30)
    #physical_status = models.CharField(max_length=30) # (SHAP)
    #Caste
    #Gothram
    #Zodiac
    #Star
    Eating_habit =  models.IntegerField(default=0, null=True, choices=get_choices(EatingHabit))
    Drinking_habit = models.IntegerField(default=0, null=True, choices=get_choices(DrinkingHabit))
    Smoking_habit = models.IntegerField(default=0, null=True, choices=get_choices(SmokingHabit))
    # Country
    # City
    # State
    # Pincode
    # Education
    contact_no = PhoneNumberField(blank=True)
    images = models.ImageField()
    about_me = models.CharField(max_length=500)
    # require_details
    marital_status = models.IntegerField(default=0, null=True, choices=get_choices(MaritalStatus))
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    email_id = models.EmailField(max_length=254)
    # password
    gender = models.IntegerField(default=0, null=True, choices=get_choices(Gender))
    #login_status =
    #profile_status =
    serving = models.BooleanField()

