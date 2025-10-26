from django.urls import path
from django.urls import path, include
from .views import RegisterView, LoginView, logout_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

# from django.urls import path
# from .views import get_users, create_user

# urlpatterns = [
# path('users/', get_users, name ='get_users'),
# path('users/create', create_user, name ='create_user')
# ]