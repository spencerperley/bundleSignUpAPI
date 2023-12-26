from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ActivateAutoDelivery
from .serializers import ActivateAutoDeliverySerializer

class ActivateAutoDeliveryCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Deserialize the incoming JSON data
        serializer = ActivateAutoDeliverySerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            # Save the validated data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
