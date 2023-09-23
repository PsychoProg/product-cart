from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.BigIntegerField()

    def __str__(self):
        return self.title 
    
    
class Course(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=255)
    price = models.BigIntegerField()
    
    def __str__(self):
        return self.title 
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        items = self.items.all()
        total = sum(item.price for item in items)
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_type = models.CharField(max_length=10)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.order.user.username} - {self.product_type} - {self.price}'

