from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response

from .models import Product, Type, User, Order, Order_item, Contact_information
from .serializers import ProductSerializer, RegisterSerializer, LoginSerializer, OrderSerializer, OrderItemSerializer, ContactInformationSerializer


class ProductView(CreateAPIView, ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['publish_date']
    # permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        type = get_object_or_404(Type, id=self.request.data.get('type_id'))
        return serializer.save(type=type)


class SingleProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serialize = self.serializer_class(request.data)
        data = serialize.data
        user = authenticate(email=data['email'], password=data['password'])
        if user != None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': str(token)})
        else:
            # raise ValueError('user was not found')
            return Response({'Error': 'user was not found'}, status=status.HTTP_400_BAD_REQUEST)


class OrderViev(CreateAPIView, ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data['order'])
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        order = serializer.instance

        user = self.request.user
        if user != AnonymousUser():
            order.user = user
            order.save()
        else:
            request.data['contact_information']['order'] = order.id
            serializer = ContactInformationSerializer(data=request.data['contact_information'])
            if serializer.is_valid():
                serializer.save()
            else:
                order.delete()
                return Response({'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        for order_item in request.data['order_items']:
            order_item['order'] = order.id
            order_item['product'] = get_object_or_404(Product, id=order_item['product_id']).id
            serializer = OrderItemSerializer(data=order_item)
            if serializer.is_valid():
                serializer.save()
            else:
                order.delete()
                return Response({'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"Success": " "})

    # def list(self, request, *args, **kwargs):
    #     queryset = Order.objects.all()
    #     for item in queryset:
    #         order = {}
    #         order_items = Order_item.objects.filter(order=item.id)
    #         contact_information = Contact_information.objects.filter(order=item.id)
    #         order['mail_number'] = item.mail_number
    #         order['city'] = item.city
    #         print(f'order: {order}')
    #     return Response({"Success": " "})



















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

# user = self.request.user
# print(f'user: {user}')
