from pyexpat import model
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=True)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=100)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)

class CustomOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=100)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    order_details = models.TextField()