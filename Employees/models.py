from django.db import models

# Create your models here.


class Person(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
