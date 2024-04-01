from django.contrib import admin

# Register your models here.
from simple_carpet.models import Category, Carpet


@admin.register()
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']
    list_display_links = ['id', 'product', 'image']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', "title", "parent"]
    list_display_links = ['id', "title"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title"]


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', "title"]
    list_display_links = ['id', "title"]
    search_fields = ['title', "category__title"]
    inlines = [ProductImageInline]
    autocomplete_fields = ["category"]
    readonly_fields = ("slug",)
