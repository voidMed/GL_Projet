from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from appointments.models import Appointment


User = get_user_model()


class AppointmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.future_date = timezone.now() + timedelta(days=1)
        self.past_date = timezone.now() - timedelta(days=1)

    def test_create_appointment(self):
        appointment = Appointment.objects.create(
            user=self.user,
            title='Test Appointment',
            description='Test description',
            date_time=self.future_date,
            duration=60,
            status='pending'
        )
        self.assertEqual(appointment.title, 'Test Appointment')
        self.assertEqual(appointment.user, self.user)
        self.assertEqual(appointment.status, 'pending')
        self.assertEqual(appointment.duration, 60)

    def test_appointment_str(self):
        appointment = Appointment.objects.create(
            user=self.user,
            title='Test Appointment',
            date_time=self.future_date
        )
        self.assertIn('Test Appointment', str(appointment))

    def test_appointment_default_status(self):
        appointment = Appointment.objects.create(
            user=self.user,
            title='Test Appointment',
            date_time=self.future_date
        )
        self.assertEqual(appointment.status, 'pending')

    def test_appointment_is_past(self):
        appointment_past = Appointment.objects.create(
            user=self.user,
            title='Past Appointment',
            date_time=self.past_date
        )
        appointment_future = Appointment.objects.create(
            user=self.user,
            title='Future Appointment',
            date_time=self.future_date
        )
        self.assertTrue(appointment_past.is_past())
        self.assertFalse(appointment_future.is_past())

    def test_appointment_ordering(self):
        date1 = timezone.now() + timedelta(days=2)
        date2 = timezone.now() + timedelta(days=1)
        date3 = timezone.now() + timedelta(days=3)
        
        Appointment.objects.create(user=self.user, title='Appointment 1', date_time=date1)
        Appointment.objects.create(user=self.user, title='Appointment 2', date_time=date2)
        Appointment.objects.create(user=self.user, title='Appointment 3', date_time=date3)
        
        appointments = Appointment.objects.all()
        self.assertEqual(appointments[0].title, 'Appointment 3')
        self.assertEqual(appointments[1].title, 'Appointment 1')
        self.assertEqual(appointments[2].title, 'Appointment 2')