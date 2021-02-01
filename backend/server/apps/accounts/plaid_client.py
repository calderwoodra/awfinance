import os

from plaid import Client
from plaid.errors import PlaidError

from apps.user.models import User


class PlaidClient:
    """ Python Plaid API client.
    """

    def __init__(self):
        self._client = Client(
            client_id=os.environ['PLAID_CLIENT_ID'],
            secret=os.environ['PLAID_SECRET'],
            environment=os.environ['PLAID_ENV'],
            api_version=os.environ['PLAID_API_VERSION'])

    def get_link_token(self, user: User):
        # Create a link_token for the given user
        response = self._client.LinkToken.create({
            'user': {
                'client_user_id': user.random_hash_id,
            },
            'products': ['transactions'],
            'client_name': 'AwsickApps',
            'country_codes': ['US'],
            'language': 'en',
            'webhook': self._get_webhook_url(),
        })
        return response['link_token']

    def get_access_token(self, public_token):
        exchange_response = self._client.Item.public_token.exchange(public_token)
        return exchange_response['access_token']

    def get_accounts(self, access_token):
        try:
            accounts_response = self._client.Accounts.get(access_token)
        except PlaidError as e:
            return {
                'error': {
                    'display_message': e.display_message,
                    'error_code': e.code,
                    'error_type': e.type
                }}
        return {
            'error': None,
            'accounts': accounts_response
        }

    @staticmethod
    def _get_webhook_url():
        # TODO(allen): create a real webhook url?
        return 'https://webhook.sample.com'
