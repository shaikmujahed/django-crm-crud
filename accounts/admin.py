from django.contrib import admin
from .models import Customer, Product, Order, Tag
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
  list_display = ['name', 'email', 'phone']
  
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'price', 'created_at']
  
class OrderAdmin(admin.ModelAdmin):
  list_display = ['status', 'created_at']
  
  
class TagAdmin(admin.ModelAdmin):
  list_display = ['name']
  
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tag, TagAdmin)