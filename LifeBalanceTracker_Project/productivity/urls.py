from django.urls import path
from . import views 
from .views import task_detail, habit_detail

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task_list'),
    # path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_list'),
    path('tasks/<int:pk>/complete/', views.mark_task_complete, name='task_complete'),
    path('tasks/<int:pk>/incomplete/', views.mark_task_incomplete, name='task_incomplete'),
    path('tasks/<int:pk>/', task_detail, name='task_detail'),
    path('habits/', views.HabitListCreateView.as_view(), name='habit-list'),
    path('habits/<int:pk>/', views.HabitDetailView.as_view(), name='habit-detail'),
    path('habits/<int:pk>/done/', views.mark_habit_done, name='habit-done'),
    path('habits/<int:pk>/not-done/', views.mark_habit_not_done, name='habit-not-done'),
    path('habits/<int:pk>/', habit_detail, name='habit_detail'),
    path('dashboard/', views.dashboard, name='dashboard'), 
]