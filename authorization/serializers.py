from rest_framework import serializers, exceptions

from core.models import User


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('password', 'password_confirm', 'username', 'first_name', 'last_name', 'email', 'phone',
                  'description', 'date_birth', 'user_type',)

    def validate_user_type(self, value):
        user = self.context.get('request').user
        if not user.is_anonymous and user.is_director:
            if user.is_admin and value == User.UserTypeChoices.director:
                raise exceptions.ValidationError('You cannot create director user')
            return value
        return User.UserTypeChoices.user

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise exceptions.ValidationError('Passwords mismatch')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_type = validated_data.get('user_type')
        is_staff = user_type in [User.UserTypeChoices.admin, User.UserTypeChoices.director]
        user = User(**validated_data, is_staff=is_staff)
        user.set_password(password)
        user.save()
        return user
