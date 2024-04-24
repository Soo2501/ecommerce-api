import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/', default='default.jpg')

    def __str__(self):
        return self.title


class Discount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.CharField(max_length=100)

    def __str__(self):
        return "Discount for " + str(self.product) + ", " + str(self.title)


class Order(models.Model):
    status_data = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
        ('refunded', 'Refunded'),
    )

    def get_order_number(self):
        _order_number = Order.objects.count() + 1
        return f"ORD-{str(_order_number).zfill(5)}"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=status_data, default='Pending')
    order_number = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.get_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title
