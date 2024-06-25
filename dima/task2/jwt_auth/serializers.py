from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        """
        Создание обьекта модели пользователя
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise serializers.ValidationError('Не удается войти в систему с предоставленными учетными данными.')
        else:
            raise serializers.ValidationError('Обязательно укажите почту и пароль.')

        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class CustomTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        """
        Создание токенов для передачи во view
        """
        refresh = RefreshToken(attrs['refresh'])

        data = {'access': str(refresh.access_token)}
        refresh.set_jti()
        refresh.set_exp()
        data['refresh'] = str(refresh)

        return data
