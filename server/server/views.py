# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def test_resp(request, *args, **kwargs):
    return Response(request)