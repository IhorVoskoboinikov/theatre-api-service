from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from theatre.models import Play, Genre, Actor
from theatre.serializers import PlayListSerializer, PlayDetailSerializer

PLAY_URL = reverse("theatre:play-list")


def sample_play(**params):
    defaults = {
        "title": "Sample play",
        "description": "Sample description",
    }
    defaults.update(params)

    return Play.objects.create(**defaults)


def sample_genre(**params):
    defaults = {
        "name": "Test genre",
    }
    defaults.update(params)

    return Genre.objects.create(**defaults)


def sample_actor(**params):
    defaults = {"first_name": "Test name", "last_name": "Test Last Name"}
    defaults.update(params)

    return Actor.objects.create(**defaults)


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


class AuthenticatedPlayApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "testuser@gmail.com", "testpass111"
        )
        self.client.force_authenticate(self.user)

    def test_list_play(self):
        sample_play()

        play_with_filter = sample_play()

        actor = sample_actor(first_name="Dwayne", last_name="Johnson")
        genre = sample_genre(name="Documentary")

        play_with_filter.actors.add(actor)
        play_with_filter.genres.add(genre)

        res = self.client.get(PLAY_URL)

        play = Play.objects.all()
        serializer = PlayListSerializer(play, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["results"], serializer.data)

    def test_list_play_with_filter_by_actors(self):
        play1 = sample_play(title="Movie1")
        play2 = sample_play(title="Movie2")
        play3 = sample_play(title="Movie2 without actors")

        actor1 = sample_actor(first_name="Dwayne", last_name="Johnson")
        actor2 = sample_actor(first_name="Angelina", last_name="Jolie")

        play1.actors.add(actor1)
        play2.actors.add(actor2)

        res = self.client.get(PLAY_URL, {"actors": {f"{actor1.id}, {actor2.id}"}})

        serializer1 = PlayListSerializer(play1)
        serializer2 = PlayListSerializer(play2)
        serializer3 = PlayListSerializer(play3)

        self.assertIn(serializer1.data, res.data["results"])
        self.assertIn(serializer2.data, res.data["results"])
        self.assertNotIn(serializer3.data, res.data["results"])

    def test_list_plays_with_filter_by_genres(self):
        play1 = sample_play(title="Movie1")
        play2 = sample_play(title="Movie2")
        play3 = sample_play(title="Movie2 without genre")

        genre1 = sample_genre(name="Documentary")
        genre2 = sample_genre(name="Comedy")

        play1.genres.add(genre1)
        play2.genres.add(genre2)

        res = self.client.get(PLAY_URL, {"genres": {f"{genre1.id}, {genre2.id}"}})

        serializer1 = PlayListSerializer(play1)
        serializer2 = PlayListSerializer(play2)
        serializer3 = PlayListSerializer(play3)

        self.assertIn(serializer1.data, res.data["results"])
        self.assertIn(serializer2.data, res.data["results"])
        self.assertNotIn(serializer3.data, res.data["results"])

    def test_filter_plays_by_title(self):
        sample_play(title="Les Misérables")
        sample_play(title="Romeo and Juliet")
        sample_play(title="The Cherry Orchard")

        res = self.client.get(PLAY_URL, {"title": {"Les"}})

        plays = Play.objects.filter(title__icontains="Les")

        serializer = PlayListSerializer(plays, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["results"], serializer.data)

    def test_detail_play(self):
        play = sample_play()

        genre1 = sample_genre(name="Genre1")
        genre2 = sample_genre(name="Genre2")

        play.genres.add(genre1, genre2)

        res = self.client.get(detail_url(play.id))

        serializer = PlayDetailSerializer(play, many=False)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_play_forbidden(self):
        data = {
            "title": "Test play",
            "description": "Test description",
        }

        res = self.client.post(PLAY_URL, data)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
