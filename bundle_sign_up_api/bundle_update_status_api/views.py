from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ActivateAutoDelivery
from .serializers import ActivateAutoDeliverySerializer

# Create your views here.
