from django.db import models

# Create your models here.
class Product(models.Model):
    title: models.CharField(max_length=50,null=False)
    price: models.ImageField()
    description: models.TextField()
    added_date: models.DateField(auto_now=True)