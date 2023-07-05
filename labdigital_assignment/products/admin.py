from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_deleted')
    list_filter = ('is_deleted',)
    actions = ['restore_selected_products']

    def restore_selected_products(self, request, queryset):
        queryset.update(is_deleted=False)

    restore_selected_products.short_description = 'Restore selected products'

admin.site.register(Product, ProductAdmin)

