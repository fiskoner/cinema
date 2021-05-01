from rest_framework import serializers, exceptions

from core.models import User


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('password', 'password_confirm', 'username', 'first_name', 'last_name', 'email', 'phone',
                  'description', 'date_birth', 'user_type', )

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise exceptions.ValidationError('Passwords mismatch')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
