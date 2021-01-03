from apps.notes.urls import notes_urlpatterns
from apps.user.urls import user_urlpatterns
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('badmin/', admin.site.urls),
]

urlpatterns += user_urlpatterns  # add URLs for authentication
urlpatterns += notes_urlpatterns  # notes URLs
