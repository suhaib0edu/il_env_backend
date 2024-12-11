from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    invited_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='invited_users')
    premium_features = models.BooleanField(default=False)
    last_version_used = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
    
