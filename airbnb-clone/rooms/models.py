from django.db import models
from django_countries.fields import CountryField  # django에서 제공하는 countries
from core import models as core_models


# 사용자가 변경을 하게 하기 위한 방법
class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Itme Model"""
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ RoomType Model Definition"""
    class Meta:
        verbose_name = 'Room Type'


class Amenity(AbstractItem):
    """ Amenity Model Definition"""
    class Meta:
        verbose_name = 'Amenities'


class Facility(AbstractItem):
    """ Facility Model Definition"""
    class Meta:
        verbose_name = 'Facilities'


class HouseRule(AbstractItem):
    """ HouseRule Model Definition"""
    class Meta:
        verbose_name = 'House Rule'


class Room(core_models.TimeStampedModel):
    """Room definition Model"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey('users.User', on_delete=models.CASCADE)
    room_type = models.ForeignKey('RoomType', on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField('Amenity', blank=True)
    facilities = models.ManyToManyField('Facility', blank=True)
    house_rules = models.ManyToManyField('HouseRule', blank=True)

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):
    """ photo model definition """
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
        