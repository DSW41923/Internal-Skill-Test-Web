from django.db import models

# Create your models here.
class Excuse(models.Model):
    provider = models.CharField(max_length=50)
    content = models.CharField(max_length=100)