from django.http import JsonResponse

def test_resp(request, *args, **kwargs):
    return JsonResponse({'message': 'Hello world'})