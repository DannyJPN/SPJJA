from django.db import models
from datetime import datetime


class Company(models.Model):
	name = models.CharField(max_length=64)

class Station(models.Model):
	name = models.CharField(max_length=32)
	created = models.DateTimeField(default=datetime.now)
	capacity = models.IntegerField()
	company = models.ForeignKey("Company",on_delete = models.CASCADE)
