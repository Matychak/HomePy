from django.contrib import admin
from .models import Product
# from data_seeder.admin import DataGeneratorAdmin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "tittle", "is_published", "price", "list_date")
    list_diaplay_links = ('id', "tittle")
    list_filter = ("category",)
    list_editable = ("is_published",)
    search_fields = ("tittle", "price", "description", "city", "category")
    list_per_page = 25


# admin.site.register(Product, DataGeneratorAdmin)
admin.site.register(Product, ProductAdmin)