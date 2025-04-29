from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin




class CustomUser(AbstractUser,PermissionsMixin):
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = "users_data"

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    stock = models.IntegerField()

    class Meta:
        db_table = "products_ecommerce"



class Transaction(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_products = models.IntegerField()
    total_price = models.IntegerField()
    transaction_mode = models.CharField(max_length=255)

    class Meta:
        db_table = "transactions_data"
