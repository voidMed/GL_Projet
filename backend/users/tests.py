from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '+1234567890',
            'address': '123 Test Street',
        }

    def test_create_user(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_user_str(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(str(user), 'testuser')

    def test_user_email_normalized(self):
        user = User.objects.create_user(
            username='testuser2',
            email='Test@EXAMPLE.COM',
            password='testpass123'
        )
        self.assertEqual(user.email, 'Test@example.com')

    def test_user_email_unique(self):
        user = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123'
        )
        self.assertEqual(user.email, 'test2@example.com')

    def test_user_username_unique(self):
        User.objects.create_user(**self.user_data)
        user_data = self.user_data.copy()
        user_data['username'] = 'testuser'
        user_data['email'] = 'different@example.com'
        with self.assertRaises(Exception):
            User.objects.create_user(**user_data)

    def test_user_fields_default_values(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.phone, '+1234567890')
        self.assertEqual(user.address, '123 Test Street')
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)