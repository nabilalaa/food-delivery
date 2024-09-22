from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "name": self.name,
            "price": self.price,
            "description": self.description
        }
