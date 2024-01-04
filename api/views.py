from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
data = [
    {
        'name': 'azizbek',
        'age': 15
    },
    {
        'name': 'elon',
        'age': 52
    },
    {
        'name': 'mark',
        'age': 39
    },

]


@api_view(http_method_names=["GET", "POST", "PUT"])
def get_products(request: Request):
    if request.method == "POST":
        print(request.data)
    elif request.method == "PUT":
        print(request.data)
    print(request.query_params)
    print(request.content_type)
    print(request.data)
    return Response(data=data)