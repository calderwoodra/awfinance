from django.conf.urls import url

from .views import api_sign_up, api_login

accounts_urlpatterns = [
    url(r'^api/v1.0/users/sign_up/$', api_sign_up, name="api_sign_up"),
    url(r'^api/v1.0/users/login/$', api_login, name="api_login"),
]
