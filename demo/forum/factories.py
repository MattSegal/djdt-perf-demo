# For creating test data
import factory
from factory.django import DjangoModelFactory

from .models import Person, Club, Thread, Comment


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = Person

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
