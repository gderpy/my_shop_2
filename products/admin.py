from django.contrib import admin
from django.utils.text import slugify
from .models import Product, Category

# SimpleListFilter - https://docs.djangoproject.com/en/5.1/ref/contrib/admin/filters/

class HasParentFilter(admin.SimpleListFilter):
    title = "Тип категории"
    parameter_name = "parent"

    def lookups(self, request, model_admin):
        return (
            ("main", "Основные категории"),
            ("sub", "Подкатегории"),
        )
    
    def queryset(self, request, queryset):
        if self.value() == "main":
            return queryset.filter(parent__isnull=True)
        elif self.value() == "sub":
            return queryset.filter(parent__isnull=False)
        return queryset
    

class SubcategoryFilter(admin.SimpleListFilter):
    title = "Фильтр подкатегорий"
    parameter_name = "subcategory_filter"

    def lookups(self, request, model_admin):
        return (
            ("sub", "Подкатегории"),
        )
    
    def queryset(self, request, queryset):
        if self.value == "sub":
            return queryset.filter(parent__isnull=False)
        return queryset


class ParentCategoryFilter(admin.SimpleListFilter):
    title = "Выберите основную категорию"
    parameter_name = "parent_category"

    def lookups(self, request, model_admin):
        if request.GET.get("subcategory_filter") == "sub":
            main_categories = Category.objects.filter(parent__isnull=True) 
            return [(category.id, category.name) for category in main_categories]
        return []
    
    def queryset(self, request, queryset):
        parent_category_id = self.value()
        if parent_category_id:
            return queryset.filter(parent_id=parent_category_id)
        return queryset


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    search_fields = ("name",)
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = (HasParentFilter, SubcategoryFilter, ParentCategoryFilter)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_available", "created_at", "category")
    list_filter = ("name", "is_available", "created_at", "category")
    search_fields = ("name", "category")
    ordering = ("-created_at",)
    list_per_page = 50
    prepopulated_fields = {"slug": ("name",)}


    
