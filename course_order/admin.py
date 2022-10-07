from django.contrib import admin
from .models import Order, OrderDetail


class OrderDetailStacked(admin.TabularInline):
    model = OrderDetail


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderDetailStacked
    ]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)
