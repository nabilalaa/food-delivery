from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# class Category(models.Model):

#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

#     class Meta:

#         verbose_name = 'categories'


# class Meal(models.Model):
#     name = models.CharField(max_length=50)
#     image = CloudinaryField("food", blank=True)
#     price = models.IntegerField()
#     description = models.TextField()
#     category = models.ForeignKey("category", on_delete=models.CASCADE, null=1)

#     def __str__(self):
#         return self.name


# class CartItem(models.Model):
#     product = models.ForeignKey(Meal, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.quantity} x {self.product.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    products = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name if self.name else "test"
