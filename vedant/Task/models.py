from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)  # Task title
    description = models.TextField()  # Detailed description
    completed = models.BooleanField(default=False)  # Task completion status
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp on creation

    def __str__(self):
        return self.title  # Display title in the admin panel