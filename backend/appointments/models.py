from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_time = models.DateTimeField()
    duration = models.IntegerField(default=60)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return f"{self.title} - {self.date_time}"

    def is_past(self):
        return self.date_time < timezone.now()