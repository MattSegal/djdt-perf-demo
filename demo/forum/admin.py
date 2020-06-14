from django.contrib import admin

from .models import User, Thread, Comment, Club

admin.site.register(User)
admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(Club)
