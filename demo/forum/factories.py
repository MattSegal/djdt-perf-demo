# For creating test data
import factory
from factory.django import DjangoModelFactory

from .models import User, Club, Thread, Comment


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Faker("first_name")


class ThreadFactory(DjangoModelFactory):
    class Meta:
        model = Thread

    title = factory.Faker("sentence", nb_words=5, variable_nb_words=True)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    text = factory.Faker("sentence", nb_words=15, variable_nb_words=True)


class ClubFactory(DjangoModelFactory):
    class Meta:
        model = Club

    text = factory.Faker("sentence", nb_words=5, variable_nb_words=True)
