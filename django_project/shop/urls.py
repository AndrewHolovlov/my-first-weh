from django.urls import path

from .views import ProductView, SingleProductView, RegisterView, LoginView, OrderViev


app_name = 'shop'

urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:pk>', SingleProductView.as_view()),
    path('account/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('order/', OrderViev.as_view() )
]
