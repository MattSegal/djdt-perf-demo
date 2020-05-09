from django.contrib import admin

from .models import Person, Thread, Comment, Club

admin.site.register(Person)
admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(Club)
