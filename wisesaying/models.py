from django.db import models

# Create your models here.
class Wisesaying(models.Model):
    content = models.TextField()
    