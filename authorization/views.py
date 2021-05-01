from django.db.models import Q

from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from authorization import serializers
from core.models import User


class UserInfoViewSet(GenericViewSet,
                      mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = serializers.UserInfoSerializer

    def get_object(self):
        return self.request.user


class UserLoginView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserLoginSerializer
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=serializers.UserLoginSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        username = data.get('username')
        user = self.queryset.filter(Q(username=username) | Q(email=username))
        if not user.exists():
            raise exceptions.NotFound('User not found')
        user = user.first()
        password = data.get('password')
        if not user.check_password(password):
            raise exceptions.PermissionDenied(detail='Wrong password')
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'Token': f'{token}'}, status=status.HTTP_200_OK)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.UserRegistrationSerializer
        return self.serializer_class
