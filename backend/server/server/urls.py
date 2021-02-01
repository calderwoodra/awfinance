from django.contrib import admin
from django.urls import path

from apps.accounts.urls import account_urlpatterns
from apps.notes.urls import notes_urlpatterns
from apps.user.urls import user_urlpatterns

urlpatterns = [
    path('badmin/', admin.site.urls),
]

urlpatterns += user_urlpatterns  # add URLs for authentication
urlpatterns += notes_urlpatterns  # notes URLs
urlpatterns += account_urlpatterns  # accounts URLs
