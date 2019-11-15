from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    summary = models.TextField(blank=True, null=False) # blank = False means it is required field
    featured = models.BooleanField(default=True)
