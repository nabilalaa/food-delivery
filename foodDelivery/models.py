from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Meal(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField("food", blank=True)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
