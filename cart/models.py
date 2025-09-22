from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'categories'



class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = CloudinaryField(null=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    session_key = models.CharField(max_length=40, null=True, blank=True, db_index=True,unique=True,)



    def __str__(self):
        return self.session_key



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items",null=True)

    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


    
    def __str__(self):
        return f"{self.product.name} - Guest"
    

    
