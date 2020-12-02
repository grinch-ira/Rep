# регистрируем все модели, чтобы админка могла с ними работать и их видела вообще
from django.contrib import admin
from shop.models import Category, Order, CartItem, Cart, Ord


def make_payed(modeladmin, request, queryset):
    queryset.update(status='Оплачен')
make_payed.short_description = 'Пометить как оплаченные'


class OrderAdmin(admin.ModelAdmin):
	list_filter = ['status']
	actions = [make_payed]

# Register your models here.
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Ord, OrderAdmin)
