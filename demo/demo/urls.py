from django.contrib import admin
from django.conf import settings
from django.urls import include, path

from forum import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("thread/<int:pk>/", views.thread, name="thread"),
    path("clubs/", views.clubs, name="club-list"),
    path("", views.home),
]


if settings.DEBUG:
    import debug_toolbar

    debug_path = path("__debug__/", include(debug_toolbar.urls))
    urlpatterns = [debug_path] + urlpatterns
