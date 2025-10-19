from rest_framework import generics, permissions
from .models import Meal, Workout, SelfCareActivity
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
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