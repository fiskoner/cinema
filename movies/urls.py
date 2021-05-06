from django.urls import path
from rest_framework.routers import SimpleRouter

from movies import views

app_name = 'movies'

router = SimpleRouter()

router.register('movie', views.MovieViewSet)

urlpatterns = [
    path('set_rating/<int:pk>', views.SetMovieRatingApiView.as_view())
]

urlpatterns += router.urls
