from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin




class CustomUser(AbstractUser,PermissionsMixin):
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = "users_data"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    stock = models.IntegerField()

    class Meta:
        db_table = "products_ecommerce"









class PaymentMode(models.TextChoices):
    UPI = 'upi', 'UPI'
    COD = 'cod', 'Cash on Delivery'
    CARD = 'card', 'Card'        

class Transaction(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_products = models.IntegerField()
    total_price = models.IntegerField()
    transaction_mode = models.CharField(max_length=10,choices=PaymentMode.choices,default=PaymentMode.UPI)
    products = models.ManyToManyField('Product', through='TransactionItem')

    class Meta:
        db_table = "transactions_data"




class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = "transaction_items"


        