from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('indoor', 'indoor'),
        ('outdoor', 'outdoor'),
    )
    name = models.CharField(max_length=12, null=True)
    price = models.IntegerField(null=True)
    category = models.CharField(max_length=12, null=True, choices=CATEGORY)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('delivered', 'delivered'),
        ('out of delivery', 'out of delivery'),
        ('pending', 'pending'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    
