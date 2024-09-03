from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from .serializers import ProductSerializer, PriceHistorySerializer
from ...models import Product, PriceHistory
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "size", "price"]
    search_fields = ["name", "description"]
    ordering_fields = ["created_time"]


class ProductDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class PriceHistory(RetrieveUpdateAPIView):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer

    def get_queryset(self, pk=1, *args, **kwargs):

        qs = super().get_queryset(*args, **kwargs)
        pst = self.request.GET.get('pst')
        if pst:
            qs = qs.filter(product=pst)

        return qs

    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({'invalid': 'bad request'})
