from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404


# User Serializer
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=get_user_model().objects.all())
        ]
    )
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    password1 = serializers.CharField(max_length=100, write_only=True)
    password2 = serializers.CharField(max_length=100, write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email','first_name', 'last_name', 'password1','password2','is_driver')
        extra_kwargs = {'password1': {'write_only': True}}

    def create(self, validated_data):
        password1 = validated_data.pop('password1')
        password2 = validated_data.pop('password2')

        if password1 != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        
        user = User.objects.create_user(validated_data['username'], validated_data['email'],password1)
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.is_driver = True
        user.save()

        return user

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user_request = get_object_or_404(
                    User,
                    email=email,
                )
        username = user_request.username

        user = authenticate(
            username=username,
            password=password
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs







    