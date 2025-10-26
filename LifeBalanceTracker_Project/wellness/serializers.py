from rest_framework import serializers
from .models import Meal, Workout, SelfCareActivity

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'meal_type', 'description', 'date']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'todays_workout', 'duration_minutes', 'date']


class SelfCareActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfCareActivity
        fields = ['id', 'activity_type', 'duration_minutes', 'notes', 'date']
    
