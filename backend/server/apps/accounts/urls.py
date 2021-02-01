from django.urls import re_path

from apps.accounts.views import get_plaid_link_token

account_urlpatterns = [
    # Get Plaid Link Token
    re_path(r'^api/v1/accounts/plaid/link_token/$', get_plaid_link_token, name='get_plaid_link_token')
]
