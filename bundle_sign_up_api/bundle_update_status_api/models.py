from django.db import models

# Create your models here.
class ActivateAutoDelivery(models.Model):
    unit = models.IntegerField()
    email = models.EmailField()
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    requestTime = models.DateField()