from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserDeleteView, UserUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('delete/', UserDeleteView.as_view(), name='delete'),
    path('update/', UserUpdateView.as_view(), name='update'),
]