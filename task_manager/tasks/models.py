from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_tasks', on_delete=models.CASCADE, default='admin')
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.task_name



