import random
from django.core.management.base import BaseCommand

from forum.models import Person, Thread, Club, Comment
from forum.factories import PersonFactory, ThreadFactory, ClubFactory, CommentFactory


class Command(BaseCommand):
    help = "Generates test data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        Person.objects.all().delete()
        Thread.objects.all().delete()
        Comment.objects.all().delete()
        Club.objects.all().delete()

        self.stdout.write("Creating new data...")
        people = []
        for _ in range(50):
            person = PersonFactory()
            people.append(person)

        for _ in range(10):
            club = ClubFactory()
            members = random.choices(people, k=8)
            club.user.add(*members)

        for _ in range(12):
            creator = random.choice(people)
            thread = ThreadFactory(creator=creator)
            for _ in range(25):
                commentor = random.choice(people)
                CommentFactory(user=commentor, thread=thread)
