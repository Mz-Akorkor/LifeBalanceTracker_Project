from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from .models import Meal, Workout, SelfCareActivity
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MealForm, WorkoutForm, SelfCareForm
from .serializers import MealSerializer, WorkoutSerializer, SelfCareActivitySerializer

# Meals
class MealListCreateView(generics.ListCreateAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MealDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)
    
@api_view(['PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def meal_detail(request, pk):
    try:
        meal = Meal.objects.get(pk=pk, user=request.user)
    except Meal.DoesNotExist:
        return Response({'error': 'Meal not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        meal.delete()
        return Response({'message': 'Meal deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MealSerializer(meal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Workouts
class WorkoutListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

@api_view(['PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def workout_detail(request, pk):
    try:
        workout = Workout.objects.get(pk=pk, user=request.user)
    except Workout.DoesNotExist:
        return Response({'error': 'Workout not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        workout.delete()
        return Response({'message': 'Workout deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = WorkoutSerializer(workout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Self-care
class SelfCareListCreateView(generics.ListCreateAPIView):
    serializer_class = SelfCareActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SelfCareActivity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SelfCareDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SelfCareActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SelfCareActivity.objects.filter(user=self.request.user)

@api_view(['PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def selfcare_detail(request, pk):
    try:
        selfcare = SelfCareActivity.objects.get(pk=pk, user=request.user)
    except SelfCareActivity.DoesNotExist:
        return Response({'error': 'Self-care activity not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        selfcare.delete()
        return Response({'message': 'Self-care activity deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = SelfCareActivitySerializer(selfcare, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@login_required
def dashboard(request):
    meals = Meal.objects.filter(user=request.user)
    workouts = Workout.objects.filter(user=request.user)
    selfcare = SelfCareActivity.objects.filter(user=request.user)
    
    return render(request, 'dashboard.html', {
        'meals': meals,
        'workouts': workouts,
        'selfcare': selfcare,
    })

def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            messages.success(request, "Meal added successfully! 🍽️")
            return redirect('wellness_dashboard')
    else:
        form = MealForm()
    return render(request, 'add_meal.html', {'form': form})

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            messages.success(request, "Workout logged successfully! 💪")
            return redirect('wellness_dashboard')
    else:
        form = WorkoutForm()
    return render(request, 'add_workout.html', {'form': form})


@login_required
def add_selfcare(request):
    if request.method == 'POST':
        form = SelfCareForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            messages.success(request, "Self-care activity added! 🧘🏾‍♀️")
            return redirect('wellness_dashboard')
    else:
        form = SelfCareForm()
    return render(request, 'add_selfcare.html', {'form': form})