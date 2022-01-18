from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import (
    authenticate,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UserLoginSerializer(serializers.Serializer):
    """Users login Serializer.

    Handle login request data.
    """

    username = serializers.CharField()
    password = serializers.CharField(min_length=5)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(
            username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credential')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(
            user=self.context.get('user'))
        return self.context['user'], token.key
    
class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    role = serializers.StringRelatedField(read_only=True)

    class Meta:
        """Meta serializer."""

        model = User
        fields = (
            'pk',
            'username',
            'email',
            'is_active',
            'is_staff',
            'first_name',
            'last_name',
            'role'
        )
        read_only_fields = ['role', 'is_staff']