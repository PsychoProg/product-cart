from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Course)

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'id']
    inlines = [OrderItemAdmin]


