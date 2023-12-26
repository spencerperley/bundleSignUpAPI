from rest_framework import serializers
from .models import ActivateAutoDelivery

class ActivateAutoDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivateAutoDelivery
        fields = '__all__'