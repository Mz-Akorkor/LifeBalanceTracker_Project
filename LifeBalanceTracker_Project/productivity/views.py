from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from .models import Task, Habit
from .forms import TaskForm, HabitForm
from wellness.models import Meal, Workout, SelfCareActivity
from .serializers import TaskSerializer, HabitSerializer

#TASK
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status=status_param)

        priority_param = self.request.query_params.get('priority')
        if priority_param:
            queryset = queryset.filter(priority=priority_param)
        
        sort_by = self.request.query_params.get('sort')
        if sort_by in ['due_date', 'priority']:
            queryset = queryset.order_by(sort_by)

        return queryset
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_query(self):
        return Task.objects(user=self.request.user)
    
    def perform_update(self, serializer):
        """Prevents editing completed task"""
        instance = self.get_object()
        if instance.status =='Completed':
            raise serializer.ValidationError('Completed task can not be edited')
        serializer.save

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_task_complete(request, pk):
    try:
        task = Task.objects(pk=pk, user=request)
        task.mark_complete()
        return Response({'message': 'Task completed successfully'})
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)
    

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])   
def mark_task_incomplete(request, pk):
    """Revert an incompleted task back to pending"""
    try:
        task = Task.objects.get(pk=pk, user=request)
        task.mark_incomplete()
        return Response({'message': 'Task reverted back to pending'})
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)
    
@api_view(['PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def task_detail(request, pk):
    """Handle updating or deleting a specific task."""
    try:
        task = Task.objects.get(pk=pk, user=request.user)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # DELETE: remove the task
    if request.method == 'DELETE':
        task.delete()
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    # PUT: update the task
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

#HABITS
class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_habit_done(request, pk):
    """Mark a habit as done"""
    try:
        habit = Habit.objects.get(pk=pk, user=request.user)
        habit.status = 'Done'
        habit.save()
        return Response({'message': 'Habit marked as done'})
    except Habit.DoesNotExist:
        return Response({'error': 'Habit not found'}, status=404)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_habit_not_done(request, pk):
    """Revert habit status to not done"""
    try:
        habit = Habit.objects.get(pk=pk, user=request.user)
        habit.status = 'Not Done'
        habit.save()
        return Response({'message': 'Habit reverted to not done'})
    except Habit.DoesNotExist:
        return Response({'error': 'Habit not found'}, status=404)
    
@api_view(['PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def habit_detail(request, pk):
    try:
        habit = Habit.objects.get(pk=pk, user=request.user)
    except Habit.DoesNotExist:
        return Response({'error': 'Habit not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        habit.delete()
        return Response({'message': 'Habit deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = HabitSerializer(habit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    habits = Habit.objects.filter(user=request.user)
    meals = Meal.objects.filter(user=request.user)
    workouts = Workout.objects.filter(user=request.user)
    selfcare = SelfCareActivity.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'habits': habits,
        'meals': meals,
        'workouts': workouts,
        'selfcare': selfcare
    })

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')  
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})