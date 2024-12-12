from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserUpdateSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from .models import CustomUser

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        
class UserDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    
    def get_object(self):
        return self.request.user

    def destroy(self, request, *args, **kwargs):
      instance = self.get_object()
      instance.delete()
      return Response({'message': 'Account deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
      

class UserUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserUpdateSerializer
    queryset = CustomUser.objects.all()

    def get_object(self):
        return self.request.user