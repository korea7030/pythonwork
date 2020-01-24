from django.db import models
from django_countries.fields import CountryField  # django에서 제공하는 countries
from core import models as core_models
from users import models as user_models


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
    pass


class Amenity(AbstractItem):
    """ Amenity Model Definition"""
    pass


class Facility(AbstractItem):
    """ Facility Model Definition"""
    pass


class HouseRule(AbstractItem):
    """ HouseRule Model Definition"""
    pass


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
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ManyToManyField(RoomType, blank=True, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
