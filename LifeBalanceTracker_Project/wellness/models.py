from django.db import models
from django.conf import settings
from django.utils import timezone

class Meal(models.Model):
    meal_category = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='meals')
    meal_type = models.CharField(max_length=20, choices=meal_category)
    description = models.TextField()
    date = models.DateField(default=timezone.now)

class Workout(models.Model):
    workout_category = [
        ('Cardio', 'Cardio'),
        ('Core', 'Core'),
        ('Quads', 'Quads'),
        ('Glutes', 'Glutes'),
        ('Stretching', 'Stretching'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workouts')
    todays_workout = models.CharField(max_length=20, choices=workout_category)
    duration_minutes = models.PositiveIntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.todays_workout} - {self.user.username}"


class SelfCareActivity(models.Model):
    activity_category = [
        ('Meditation', 'Meditation'),
        ('Reading', 'Reading'),
        ('Journaling', 'Journaling'),
        ('No Screens', 'No Screens'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='selfcare_activities')
    activity_type = models.CharField(max_length=20, choices=activity_category)
    duration_minutes = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.activity_type} - {self.user.username}"
