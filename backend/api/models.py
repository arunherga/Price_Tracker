from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=100)
    item_url = models.CharField(max_length=2000)
    item_price = models.IntegerField(max_length=50)
    time = models.DateTimeField(max_length=50)



