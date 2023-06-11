from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.

def today():
    return timezone.now()

class Todo(models.Model):
    title = models.TextField(max_length=250)   # task name
    description = models.TextField(max_length=500, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='assigned_to')
    due_date = models.DateField(default=today)

    class Meta:
        ordering = ['due_date']
