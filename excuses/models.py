from django.db import models

# Create your models here.
class Excuse(models.Model):
    content = models.CharField(max_length=100)