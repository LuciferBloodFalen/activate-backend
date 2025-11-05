from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    class statusChoices(models.IntegerChoices):
        DONE = 1, 'done'
        PENDING = 0, 'pending'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    status = models.PositiveIntegerField(choices=statusChoices, default=statusChoices.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)