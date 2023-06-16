from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.

def today():
    return timezone.now()

class Tag(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.TextField(max_length=100)   # task name
    description = models.TextField(max_length=500, null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, related_name='tag')
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='assigned_to')
    due_date = models.DateField(default=today)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title

