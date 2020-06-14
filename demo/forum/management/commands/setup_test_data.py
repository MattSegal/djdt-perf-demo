import random

from django.db import transaction
from django.core.management.base import BaseCommand

from forum.models import User, Thread, Club, Comment
from forum.factories import UserFactory, ThreadFactory, ClubFactory, CommentFactory


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        User.objects.all().delete()
        Thread.objects.all().delete()
        Comment.objects.all().delete()
        Club.objects.all().delete()
        self.stdout.write("Creating new data...")
        people = []
        for _ in range(50):
            person = UserFactory()
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
