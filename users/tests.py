# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse

from rest_framework_jwt.settings import api_settings

from django.contrib.auth import get_user_model

# from django.urls import reverse
# Create your tests here.

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserAPITestCase(APITestCase):

    def setUp(self):
        user = User.objects.create_user(username='testuser', email='testuser@gmail.com')
        user.set_password('testuserpwd')
        user.save()

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_post_login_existed_user(self):
        login_url = reverse('login')
        data = {
            'email': 'testuser@gmail.com',
            'password': 'testuserpwd'
        }
        response = self.client.post(login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_login_not_existed_user(self):
        login_url = reverse('login')
        data = {
            'email': 'testuser1@gmail.com',
            'password': 'testuserpwd'
        }
        response = self.client.post(login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_users_list_without_auth(self):
        list_view_url = reverse('list-view')
        response = self.client.get(list_view_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_users_list_with_auth(self):
        list_view_url = reverse('list-view')
        user_obj = User.objects.first()
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.get(list_view_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_correct_registration(self):
        register_url = reverse('register')
        data = {
            'email': 'testuser2@gmail.com',
            'username': 'testuser2',
            'password': 'testuserpwd',
            'password2': 'testuserpwd',
        }
        response = self.client.post(register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_incorrect_registration(self):
        register_url = reverse('register')
        data = {}
        response = self.client.post(register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_detail_auth(self):
        user_detail_view_url = reverse('detail-view')
        user_obj = User.objects.first()
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.get(user_detail_view_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail_no_auth(self):
        user_detail_view_url = reverse('detail-view')
        data = {}
        response = self.client.get(user_detail_view_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
