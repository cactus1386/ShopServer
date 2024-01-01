from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ProductSerializer
from ...models import Product
from django.shortcuts import get_object_or_404


# The class for get and create products
class ProductList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer

    # Get function
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    # Post function
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class ProductDetail(APIView):
    serializer_class = ProductSerializer

    def get(self, request, id):
        product = Product.objects.get(pk=id)
        serializer = self.serializer_class(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        product = Product.objects.get(pk=id)
        product.delete()
        return Response({'detail':'Item delete successfully'}, status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def productDetail(request, id):
#     # product = get_object_or_404(Product, pk=id)
#     product = Product.objects.get(pk=id)
#     if request.method == "GET":
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         product.delete()
#         return Response({'detail':'Item delete successfully'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def productList(request):
#     products = Product.objects.all()
#     if request.method == "GET":
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)