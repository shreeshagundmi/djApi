from django.db import models

# Create your models here.
class Crud_Users(models.Model):
    name = models.CharField(max_length=70)