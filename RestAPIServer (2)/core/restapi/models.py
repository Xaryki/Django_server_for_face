from django.db import models

# Create your models here.
class Photos(models.Model):
    path = models.ImageField()