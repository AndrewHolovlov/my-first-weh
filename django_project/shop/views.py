from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView, CreateAPIView,ListAPIView ,get_object_or_404, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin

from .models import Product, Type
from .serializers import ProductSerializer


class ProductView(CreateAPIView, ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['publish_date']

    def perform_create(self, serializer):
        type = get_object_or_404(Type, id=self.request.data.get('type_id'))
        return serializer.save(type=type)


class SingleProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





















# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
#
# from .models import Product, Type
# from .serializers import ProductSerializer
#
# class ProductView(APIView):
#     def get(self, request):
#         print(f'request: {request}')
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response({"products": serializer.data})
#
#     def post(self, request):
#         print(f'method: {request.method}')
#         print(f'url: {request.get_full_path()}')
#         print(f'request.data: {request.data}')
#         product = request.data.get('product')
#         serializer = ProductSerializer(data=product)
#         if serializer.is_valid():
#             product_saved = serializer.save()
#             return Response({"success": "Product '{}' created successfully".format(product_saved.name)})
#         else:
#             print(f'serializer.errors: {serializer.errors}')
#             return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def put(self, request, pk):
#         saved_product = get_object_or_404(Product.object.all(), pk=pk)
#         data = request.data.get('product')
#         serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             product_saved = serializer.save()
#         return Response({"success": "Product '{}' updated successfully".format(product_saved.name)})
#
#     def delete(self, request, pk):
#         product = get_object_or_404(Product.object.all(), pk=pk)
#         product.delete()
#         return Response({"message": "Product with id '{}' has been deleted".format(pk)}, status=204)