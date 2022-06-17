from django.db import models

# Create your models here.
class Comment(models.Model):
    description=models.TextField(blank=True)
