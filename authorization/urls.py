from django.urls import path
from rest_framework import routers

from authorization import views

app_name = 'authorization'

router = routers.SimpleRouter()

router.register('user', views.UserViewSet)

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('user_info/', views.UserInfoViewSet.as_view({'get': 'retrieve'})),
]

urlpatterns += router.urls
