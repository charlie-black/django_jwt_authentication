from django.urls import path
from .views import CustomUserRegistrationView, CustomTokenObtainPairView, UserProfileView

urlpatterns = [
    # User registration URL
    path('api/register/', CustomUserRegistrationView.as_view(), name='user-registration'),

    # User login URL to obtain JWT token
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),

    # Example protected view that requires authentication
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
]
