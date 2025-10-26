from django.urls import path
from . import views

urlpatterns = [
    path('meals/', views.MealListCreateView.as_view(), name='meal-list-create'),
    path('meals/<int:pk>/', views.MealDetailView.as_view(), name='meal-detail'),
    path('meals/<int:pk>/', views.meal_detail, name='meal-detail'),
    path('workouts/', views.WorkoutListCreateView.as_view(), name='workout-list-create'),
    path('workouts/<int:pk>/', views.WorkoutDetailView.as_view(), name='workout-detail'),
    path('workouts/<int:pk>/', views.workout_detail, name='workout-detail'),
    path('selfcare/', views.SelfCareListCreateView.as_view(), name='selfcare-list-create'),
    path('selfcare/<int:pk>/', views.SelfCareDetailView.as_view(), name='selfcare-detail'),
    path('selfcare/<int:pk>/', views.selfcare_detail, name='selfcare-detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
]