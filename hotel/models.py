from django.db import models
from django.utils import timezone

class Dish(models.Model):
	dish_type = models.CharField(max_length=200)
	dish_category = models.CharField(max_length=50)
	dish_name = models.CharField(max_length=100)
	dish_description = models.TextField()
	dish_price = models.IntegerField()

	def __str__(self):
		return self.type

