import json
from django.test import TestCase, Client

from rest_framework import status
from .models import ActivateAutoDelivery

class ActivateAutoDeliveryCreateViewTest(TestCase):
    def test_create_activate_auto_delivery(self):
        client = Client()

        # Load test data from the JSON file
        with open('bundle_update_status_api/testData/test_ActivateAutoDelivery_body.json') as file:
            test_data = json.load(file)

        # Send a POST request to your API endpoint
        response = client.post('/ActivateAutoDelivery/', data=test_data, content_type='application/json')

        # Check that the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Optionally, check the created object in the database
        created_object = ActivateAutoDelivery.objects.last()
        self.assertEqual(created_object.unit, test_data['unit'])
        self.assertEqual(created_object.complex, test_data['complex'])
        self.assertEqual(created_object.email, test_data['email'])
        self.assertEqual(created_object.firstName, test_data['firstName'])
        self.assertEqual(created_object.lastName, test_data['lastName'])
        self.assertEqual(str(created_object.requestTime), test_data['requestTime'])