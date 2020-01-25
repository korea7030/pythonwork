from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    )

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_KOREAN = 'kr'
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_KOREAN, 'Korean')
    )

    CURRENCY_USE = 'usd'
    CURRENCY_KRW = 'krw'
    CURRENCY_CHOICES = (
        (CURRENCY_USE, 'USD'),
        (CURRENCY_KRW, 'KRW')
    )

    avatar = models.ImageField(upload_to='avatars', blank=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True
    )
    superhost = models.BooleanField(default=False)
