from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")  # Assign tasks to users
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    duedate = models.DateTimeField()
    tag = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']  # Orders by most recent first

