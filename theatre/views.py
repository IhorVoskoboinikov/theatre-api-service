from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from theatre.models import Genre, Actor
from theatre.serializers import GenreSerializer, ActorSerializer


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class ActorViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
