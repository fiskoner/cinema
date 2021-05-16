import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status

from core.models import User


@pytest.mark.django_db
def test_user_create():
    user = User.objects.create_user(
        'test_user', 'test_user@mail.com', 'test_user_password', user_type=User.UserTypeChoices.user
    )
    assert user.username == 'test_user'
    assert user.email == 'test_user@mail.com'
    assert user.check_password('test_user_password')
    assert user.user_type == User.UserTypeChoices.user


@pytest.mark.django_db
def test_user_create_and_login(client: Client):
    url = reverse('authorization:login')
    user = User.objects.create_user(
        'test_user', 'test_user@mail.com', 'test_user_passwd', user_type=User.UserTypeChoices.user
    )
    data = {
        'username': user.username,
        'password': 'test_user_passwd'
    }
    response = client.post(url, data=data)
    assert response.status_code == status.HTTP_200_OK