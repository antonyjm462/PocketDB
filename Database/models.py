from django.db import models

# Create your models here.
class Database(models.Model):
    _id = models.CharField(max_length=100)
    _data = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 