from django.test import TestCase
from django.test import Client
# Create your tests here.
class BookInfo(TestCase):
	c = Client()
	response = c.get('/book/')
	print(response.status_code)