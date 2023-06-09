from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.TextField(max_length=250)   # task name
    description = models.TextField(max_length=500, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_by = models.CharField(max_length=150, default='Anonymous')
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
