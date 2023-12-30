from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from ...models import Product
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"])
def productList(request):
    products = Product.objects.all()
    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def productDetail(request, id):
    # product = get_object_or_404(Product, pk=id)
    product = Product.objects.get(pk=id)
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        return Response({'detail':'Item delete successfully'}, status=status.HTTP_204_NO_CONTENT)


