from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'categories'


class Item(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField("food", blank=True)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey("category", on_delete=models.CASCADE, null=1)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
