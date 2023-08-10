from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from theatre.models import Play, Performance, TheatreHall, Genre, Actor

PLAY_URL = reverse("theatre:play-list")
PERFORMANCE_URL = reverse("theatre:performance-list")


def sample_play(**params):
    defaults = {
        "title": "Sample play",
        "description": "Sample description",
    }
    defaults.update(params)

    return Play.objects.create(**defaults)


def sample_genre(**params):
    defaults = {
        "name": "Drama",
    }
    defaults.update(params)

    return Genre.objects.create(**defaults)


def sample_actor(**params):
    defaults = {"first_name": "Test name", "last_name": "Test Last Name"}
    defaults.update(params)

    return Actor.objects.create(**defaults)


def sample_performance(**params):
    theatre_hall = TheatreHall.objects.create(name="Blue", rows=20, seats_in_row=20)

    defaults = {
        "show_time": "2022-06-02 14:00:00",
        "movie": None,
        "theatre_hall": theatre_hall,
    }
    defaults.update(params)

    return Performance.objects.create(**defaults)


def detail_url(play_id):
    return reverse("theatre:play-detail", args=[play_id])


class UnauthenticatedPlayApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(PLAY_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AdminPlayApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_superuser(
            "admin@gmail.com",
            "adminpass111",
            is_staff=True,
        )
        self.client.force_authenticate(self.user)

    def test_create_play(self):
        genre = sample_genre()
        actor = sample_actor()

        data = {
            "title": "Test movie",
            "description": "Test description",
            "genres": [genre.id],
            "actors": [actor.id],
        }

        res = self.client.post(PLAY_URL, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_delete_play_not_allowed(self):
        movie = sample_play()
        url = detail_url(movie.id)

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

