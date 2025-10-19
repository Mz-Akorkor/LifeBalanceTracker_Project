from rest_framework import serializers
from .models import Meal, Workout, SelfCareActivity

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
        read_only_fields = ['user']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'
        read_only_fields = ['user']


class SelfCareActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfCareActivity
        fields = '__all__'
        read_only_fields = ['user']
