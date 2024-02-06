from django.db import models
from django.contrib.auth.models import User

class userdetails(models.Model):
    USER_TYPE_CHOICES = [
        ('Government', 'Government'),
        ('Normal', 'Normal'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    user_phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.user.username} ({self.user_type})'