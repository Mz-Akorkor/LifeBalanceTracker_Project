from django.urls import path
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# from django.urls import path
# from .views import get_users, create_user

# urlpatterns = [
# path('users/', get_users, name ='get_users'),
# path('users/create', create_user, name ='create_user')
# ]