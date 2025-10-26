from django.db import models
from django.conf import settings
from django.utils import timezone

class Task(models.Model):
    priority_level = [
        ('Low', 'Low'), 
        ('Medium', 'Medium'),
        ('High', 'High')
    ]

    task_status = [
        ('Pending', 'Pending'),
        ('Started', 'Started'),
        ('Completed','Completed')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=priority_level, default='Medium')
    status = models.CharField(max_length=10, choices=task_status, default='Pending')
    user_task_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.status})"
    
    def mark_complete(self):
        """Mark task as complete and store timestamp"""
        self.status = 'Completed'
        self.completed_at = timezone.now()
        self.save()

    def mark_complete(self):
        """Revert task to imcomple"""
        self.status = 'Pending'
        self.completed_at = None
        self.save()

class Habit(models.Model):
    task_frequency = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly')
    ]

    achievement_status = [
        ('Done', 'Done'),
        ('Not Done', 'Not Done'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=200)
    frequency = models.CharField(max_length=20, choices=task_frequency)
    status = models.CharField(max_length=20, choices=achievement_status, default='Not Done')

    def __str__(self):
        return f"{self.name} ({self.frequency})"
    
