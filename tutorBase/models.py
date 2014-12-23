from django.db import models
from os import urandom

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    salt = models.IntegerField(default=urandom(50))

class TutorCard(models.Model):
    tutor = models.ForeignKey(User)
    first_name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    tagLine = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    rate = models.CommaSeparatedIntegerField(max_length=10)
    phone = models.IntegerField()