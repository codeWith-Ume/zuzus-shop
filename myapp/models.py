from django.db import models

# Create your models here.
class Order(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name