from django.db import models

# Create your models here.
class ActivateAutoDelivery(models.Model):
    unit = models.IntegerField()
    complex = models.CharField(max_length=255,null = True)
    email = models.EmailField()
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    requestTime = models.DateField()
    