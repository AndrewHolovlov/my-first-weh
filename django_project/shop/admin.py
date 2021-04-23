from django.contrib import admin
from .models import Product, Type, User, Order, Order_item, Contact_information


class OrderItemInline(admin.TabularInline):
    model = Order_item
    raw_id_fields = ['product']


class ContactInline(admin.TabularInline):
    model = Contact_information



class OrderAdmin(admin.ModelAdmin):
    list_display = ['mail_number', 'city', 'created_at']
    inlines = [OrderItemInline, ContactInline]


admin.site.register(Product)
admin.site.register(Type)
admin.site.register(User)
admin.site.register(Order, OrderAdmin)
