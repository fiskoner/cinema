from rest_framework import routers

from directory import views

app_name = 'directory'

router = routers.SimpleRouter()

router.register('actor', views.ActorViewSet)
router.register('actor_movies', views.ActorMovieViewSet)
router.register('movie_director', views.MovieDirectorViewSet)
router.register('movie_genre', views.MovieGenreViewSet)

urlpatterns = []

urlpatterns += router.urls