from django.test import TestCase
from django.contrib.auth import get_user_model
from notifications.models import Notification


User = get_user_model()


class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_create_notification(self):
        notification = Notification.objects.create(
            user=self.user,
            title='Test Notification',
            message='This is a test notification',
            notification_type='email'
        )
        self.assertEqual(notification.title, 'Test Notification')
        self.assertEqual(notification.user, self.user)
        self.assertEqual(notification.notification_type, 'email')
        self.assertFalse(notification.is_read)

    def test_notification_str(self):
        notification = Notification.objects.create(
            user=self.user,
            title='Test Notification',
            message='Test message'
        )
        self.assertIn('Test Notification', str(notification))
        self.assertIn('testuser', str(notification))

    def test_notification_default_type(self):
        notification = Notification.objects.create(
            user=self.user,
            title='Test Notification',
            message='Test message'
        )
        self.assertEqual(notification.notification_type, 'email')

    def test_notification_mark_as_read(self):
        notification = Notification.objects.create(
            user=self.user,
            title='Test Notification',
            message='Test message'
        )
        self.assertFalse(notification.is_read)
        notification.is_read = True
        notification.save()
        self.assertTrue(Notification.objects.get(pk=notification.pk).is_read)

    def test_notification_ordering(self):
        notification1 = Notification.objects.create(
            user=self.user,
            title='Notification 1',
            message='Message 1'
        )
        notification2 = Notification.objects.create(
            user=self.user,
            title='Notification 2',
            message='Message 2'
        )
        notifications = Notification.objects.all()
        self.assertEqual(notifications[0], notification2)
        self.assertEqual(notifications[1], notification1)