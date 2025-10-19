from django.urls import path
from . import views  # 👈🏾 Add this line

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', views.mark_task_complete, name='task-complete'),
    path('tasks/<int:pk>/incomplete/', views.mark_task_incomplete, name='task-incomplete'),

    path('habits/', views.HabitListCreateView.as_view(), name='habit-list'),
    path('habits/<int:pk>/', views.HabitDetailView.as_view(), name='habit-detail'),
    path('habits/<int:pk>/done/', views.mark_habit_done, name='habit-done'),
    path('habits/<int:pk>/not-done/', views.mark_habit_not_done, name='habit-not-done'),
]