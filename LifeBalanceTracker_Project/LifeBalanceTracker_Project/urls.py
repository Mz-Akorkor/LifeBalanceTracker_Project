from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from productivity.views import dashboard
from productivity.views import dashboard, add_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('productivity/', include('productivity.urls')),
    path('wellness/', include('wellness.urls')),
    path('', dashboard, name='dashboard'),
    path('add-task/', add_task, name='add_task'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/productivity/', include('productivity.urls')),
]
