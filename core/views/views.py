from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
from rest_framework.decorators import api_view


@api_view(['GET'])
def index_api(request):
    return JsonResponse({"data":"welcome!!"},status=200)
