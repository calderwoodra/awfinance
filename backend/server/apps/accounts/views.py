import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import AwsickUser, create_new_user


@csrf_exempt
@require_http_methods(['POST'])
def api_sign_up(request):
    json_body = json.loads(request.body.decode('utf-8'))
    username = json_body.get('username')
    password = json_body.get('password')
    if not username:
        return JsonResponse({'error_message': 'Username required.'}, status=400)
    elif not password:
        return JsonResponse({'error_message': 'Password required.'}, status=400)
    return create_new_user(username, password)


@csrf_exempt
@require_http_methods(['POST'])
def api_login(request):
    json_body = json.loads(request.body.decode('utf-8'))
    username = json_body.get('username')
    password = json_body.get('password')
    django_user = authenticate(username=username, password=password)
    if django_user is None:
        return JsonResponse({'error_message': 'User does not exist.'}, status=400)

    user = AwsickUser.objects.get(user=django_user)
    if user is None:
        return JsonResponse({'error_message': 'There was an issue. Contact support.'}, status=400)

    return JsonResponse({"token": django_user.token}, status=200)
