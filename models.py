from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse


        # -------------------------------------
# bảng User
class User(models.Model) :
    user_name = models.CharField(max_length=1000)  
    user_email = models.CharField(max_length=1000) 
    user_passwords = models.CharField(max_length=1000)  
    user_phone = models.CharField(max_length=1000)  
    user_address =  models.TextField(max_length=500, blank=True, null=True)   
   
# bảng Products
class Product(models.Model) :
    categories_id = models.CharField(max_length=1000)
    product_title = models.CharField(max_length=1000) 
    product_price = models.PositiveIntegerField()
    product_desc = models.TextField(max_length=500, blank=True, null=True)
    product_images = models.ImageField(upload_to='products/', null=True)
# bảng Categories
class Categories(models.Model):
    categories_title = models.CharField(max_length=200)

# bảng Cart
class Cart(models.Model):
    product_id = models.CharField(max_length=1000)
    user_id = models.CharField(max_length=1000)
    quality = models.IntegerField(null=True, blank=True)

# bảng  Order
class Order(models.Model):
    product_id = models.CharField(max_length=1000)
    user_id = models.CharField(max_length=1000)
    quality = models.IntegerField(null=True, blank=True)
    ngaythang = models.DateTimeField(auto_now_add=True)
    tinhtrang = models.CharField(max_length=1000)

# bảng Contact
class Contact(models.Model):
    user_id = models.CharField(max_length=1000)
    message = models.TextField(max_length=500, blank=True, null=True)
    day = models.DateTimeField(auto_now_add=True)
