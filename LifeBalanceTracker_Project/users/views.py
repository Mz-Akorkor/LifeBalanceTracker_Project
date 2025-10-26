from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, get_user_model
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import CustomUser

User = get_user_model()


# ✅ REGISTER NEW USER
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Override default create() to return a success message and JWT tokens."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Get tokens
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        dashboard_url = request.build_absolute_uri(reverse('dashboard'))

        return Response(
            {
                "message": "Registration successful 🎉",
                "user": serializer.data,
                "refresh": str(refresh),
                "access": str(access),
                "dashboard_url": dashboard_url,
            },
            status=status.HTTP_201_CREATED,
        )


# ✅ LOGIN VIEW
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data 

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "message": "Login successful ✅",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "dashboard_url": request.build_absolute_uri(reverse('dashboard')),
            },
            status=status.HTTP_200_OK,
        )


# ✅ LOGOUT VIEW (JWT BLACKLIST)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Blacklists the refresh token (used for JWT logout)."""
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Logout successful 👋🏾"},
                status=status.HTTP_205_RESET_CONTENT,
            )

        except Exception as e:
            print("Logout error:", e)
            return Response(
                {"error": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST,
            )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    """Logs out the current user (session-based)."""
    logout(request)
    return Response(
        {"message": "You have been logged out successfully 👋🏾"},
        status=status.HTTP_200_OK,
    )
