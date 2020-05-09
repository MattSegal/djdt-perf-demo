from django.shortcuts import render

from .models import Person, Thread, Comment, Club


def home(request):
    """
    Show all threads
    """
    # Slow version
    threads = []
    thread_pks = Thread.objects.all().values_list("pk", flat=True)
    for pk in thread_pks:
        thread = Thread.objects.get(pk=pk)
        threads.append(thread)

    # Faster version
    # threads = Thread.objects.all()

    # Fastest version
    # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#select-related
    # threads = Thread.objects.select_related("creator").all()

    context = {"threads": threads}
    return render(request, "forum/home.html", context)


def thread(request, pk):
    """
    Show all the comments in a thread
    """
    # Slow version
    thread = Thread.objects.get(pk=pk)

    # Faster version
    # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#prefetch-related
    # thread = Thread.objects.prefetch_related("comment_set__user").get(pk=pk)

    context = {"thread": thread}
    return render(request, "forum/thread.html", context)


def clubs(request):
    """
    Show all threads
    """
    # Slow version
    clubs = Club.objects.all()

    # Faster version
    # clubs = Club.objects.prefetch_related("user").all()

    context = {"clubs": clubs}
    return render(request, "forum/club-list.html", context)
