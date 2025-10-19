from rest_framework import serializers
from .models import Task, Habit
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'
        only_read_fields = ['user', 'completed_at']

    def validate_due_date(self,value):
        if value < date.today():
            raise serializers.ValidationError("Due date must be today or in the future.")
        return value
    
class HabitSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Habit
        fields = '__all__'
        only_read_fields = ['user']