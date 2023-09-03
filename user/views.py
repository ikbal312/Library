from django.shortcuts import get_object_or_404 as _get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .permissions import ProfilePermission
from  .models import User
from rest_framework import mixins
class RegistrationView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response('Successfully Registered', status=status.HTTP_201_CREATED, headers=headers)


registration_view = RegistrationView.as_view()


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


login_view = LoginView.as_view()


class RefreshTokenView(TokenRefreshView):
    permission_classes = [IsAuthenticated]


refresh_token_view = RefreshTokenView.as_view()


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [ProfilePermission]
    queryset = User.objects.all()


    def get_object(self):
        qs = self.get_queryset()
        user = self.request.user
        return _get_object_or_404(qs,email=user)

    
    
profile_view = ProfileView.as_view()