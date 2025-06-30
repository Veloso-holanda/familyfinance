from django.contrib import admin
from finances.models import Revenue, CashOutFlow, Category


class RevenueAdmin(admin.ModelAdmin):
    list_display = ('value','source')
    search_fields = ('source',)


class CashOutFlowAdmin(admin.ModelAdmin):
    list_display = ('value','category','payment_method', 'payment_type','installments',)
    search_fields = ('category','payment_method', 'payment_type',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Revenue, RevenueAdmin)
admin.site.register(CashOutFlow, CashOutFlowAdmin)
admin.site.register(Category, CategoryAdmin)