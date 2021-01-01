from apps.accounts.urls import accounts_urlpatterns
from apps.notes.urls import notes_urlpatterns
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += accounts_urlpatterns  # add URLs for authentication
urlpatterns += notes_urlpatterns  # notes URLs
