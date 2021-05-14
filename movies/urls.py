from django.urls import path
from rest_framework.routers import SimpleRouter

from movies import views

app_name = 'movies'

router = SimpleRouter()

router.register('movie', views.MovieViewSet)
router.register('my_ratings', views.UserRatingsViewSet)
router.register('subscription', views.SubscriptionViewSet)

urlpatterns = [
    path('set_rating/<int:pk>', views.SetMovieRatingAPIView.as_view()),
    path('set_time_watched/<int:pk>', views.SetMovieTimeWatchedAPIView.as_view()),
    path('movie/stream_video/<int:pk>/<int:quality>', views.MovieViewSet.as_view({'get': 'stream_video'})),
]

urlpatterns += router.urls
