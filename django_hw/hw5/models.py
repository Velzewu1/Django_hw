from django.db import models

class Kiosk(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    description = models.TextField()
    location = models.TextField()
    contact = models.EmailField()
class Icecream(models.Model):
    kiosk = models.ForeignKey(Kiosk, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
