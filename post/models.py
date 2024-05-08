from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    discount_price = models.IntegerField(blank=True)
    remainder =  models.IntegerField(default=0)
    characteristics = models.CharField(max_length=10000)
    # category =