from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import RegisterSerializer, LoginSerializer, CustomTokenRefreshSerializer


class RegisterAPIView(generics.CreateAPIView):
    """
    Регистрация
    """
    serializer_class = RegisterSerializer


class LoginAPIView(generics.GenericAPIView):
    """
    Авторизация
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class CustomTokenRefreshView(TokenRefreshView):
    """
    Обновление access и refresh токенов через старый refresh токен
    """
    serializer_class = CustomTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        refresh = serializer.validated_data['refresh']
        access = serializer.validated_data['access']

        return Response({
            'refresh': refresh,
            'access': access
        })
