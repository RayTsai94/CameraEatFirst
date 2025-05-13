from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class CheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkins')
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    location = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-time']
        unique_together = ['user', 'date']

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"
