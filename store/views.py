from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product, Discount, Category, Order
from .serializers import ProductSerializer, DiscountSerializer, CategorySerializer, OrderItemSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


@swagger_auto_schema(tags=['category'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', "delete"]
    search_fields = ['title', ]
    filterset_fields = ['title', ]


@swagger_auto_schema(tags=['product'])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['title', ]
    filterset_fields = ['title', ]


@swagger_auto_schema(tags=['discount'])
class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    http_method_names = ['get', 'post', 'delete']


@swagger_auto_schema(tags=['order'], methods=['post'], request_body=OrderItemSerializer)
@api_view(['POST'])
def orderItemView(request):
    if request.method == 'POST':
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            product = Product.objects.get(title=serializer.data['title'])
            product.stock -= serializer.data['quantity']
            product.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
