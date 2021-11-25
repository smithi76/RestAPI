from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from emploapp.models import employee, stud, cust
import json
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from emploapp.views import Custlist

# class TestViews(TestCase):
#     def test_student_list_GET(self):
#         client = Client()
#         response = client.get(reverse('stude-list'))
#         print('fhhhhhhhhhhhhhhhhhhh')
#         self.assertEquals(response.status_code, 200)
#         # self.assertTemplateUsed(response, )

class TestUrls(SimpleTestCase):
    def test_empl_list_url_is_resloved(self):
        url = reverse('cust-list')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Custlist)

class CustAPIViewTests(APITestCase):
    cust_url = reverse('cust -list')
    stud_url = reverse('stud-create')

    def setUp(self):
        self.user = User.objects.create_user(username='admin1', password='some-strong-password1')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)

    def tearDown(self):
        pass

    def test_get_employees_authenticated(self):
        response = self.client.get(self.cust_url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customer_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.cust_url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_customer_authenticated(self):

        data = {
            "name": 'Lal',
            "product": 'Rice',
            "cust_id": '105'
        }

        response = self.client.post(self.stud_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Lal')









