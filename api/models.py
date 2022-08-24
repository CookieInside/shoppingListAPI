from django.db import models



class ShoppingItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=0)
    qrCodeId = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    oldLocations = models.CharField(max_length=1000)
    def __str__(self):
        return str([self.name, self.price, self.qrCodeId, self.location, self.oldLocations])