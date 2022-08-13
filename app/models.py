from django.db import models
from django.urls import reverse

class Course(models.Model):
    image = models.ImageField()
    result = models.ImageField(null=True)
    