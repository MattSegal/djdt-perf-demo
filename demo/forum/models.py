from django.db import models


class Person(models.Model):
    """
    A person who uses the website
    """

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Thread(models.Model):
    """
    A comment thread
    """

    title = models.CharField(max_length=128)
    creator = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    A comment by a user on a thread
    """

    text = models.CharField(max_length=128)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)


class Club(models.Model):
    """
    A group of users
    """

    text = models.CharField(max_length=128)
    user = models.ManyToManyField(Person)
