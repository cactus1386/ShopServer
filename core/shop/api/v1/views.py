from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def productList(request):
    return Response("ok")

@api_view()
def productDetail(request, id):
    return Response(id)