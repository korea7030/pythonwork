from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from jsonfield import JSONField
from django.urls import reverse
from .payments import BaseOrder
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    icon = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_detail', args=[self.pk])


class Shop(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(blank=True)
    latlng = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)
    meta = JSONField()  # PostgreSQL의 JSONField와 다르다

    def __str__(self):
        return self.name

    @property
    def address(self):
        return self.meta.get('address')

    def get_absolute_url(self):
        return reverse('shop:shop_detail', args=[self.category_id, self.pk])


class Review(models.Model):
    shop = models.ForeignKey(Shop)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    photo = models.ImageField(blank=True)
    rating = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.message


class Item(models.Model):
    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(blank=True)
    amount = models.PositiveIntegerField()
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)
    meta = JSONField()

    def __str__(self):
        return self.name


class Order(BaseOrder):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, validators=[RegexValidator(r'010[1-9]\d{7}$')])


class OrderItem(models.Model):
    item = models.ForeignKey(Item)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order)

    @property
    def amount(self):
        return self.quantity * self.item.amount
