from django import forms
from .models import Meal, Workout, SelfCareActivity

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_type', 'description', 'date']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['todays_workout', 'duration_minutes', 'date']

class SelfCareForm(forms.ModelForm):
    class Meta:
        model = SelfCareActivity
        fields = ['activity_type', 'duration_minutes', 'notes', 'date']