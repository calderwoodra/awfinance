from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from apps.accounts.plaid_client import PlaidClient


@csrf_exempt
@require_http_methods(['GET'])
def get_plaid_link_token(request):
    if request.method != 'GET':
        return JsonResponse(
            {'error_message': 'Illegal request method: ' + request.method},
            status=400)

    print(type(request))
    plaid_client = PlaidClient()
    token = plaid_client.get_link_token(request.user)
    return JsonResponse({'link_token': token, }, status=200)
