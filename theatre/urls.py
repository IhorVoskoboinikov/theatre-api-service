from django.urls import path, include
from rest_framework import routers

from theatre.views import (
    GenreViewSet,
    ActorViewSet,
    TheatreHallViewSet,
    PlayViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("theatres", TheatreHallViewSet)
router.register("plays", PlayViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
