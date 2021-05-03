from rest_framework.routers import SimpleRouter

from movies import views

app_name = 'movies'

router = SimpleRouter()

router.register('movie', views.MovieViewSet)

urlpatterns = []

urlpatterns += router.urls
