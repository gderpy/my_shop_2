from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL-slug")
    parent = models.ForeignKey("self", on_delete=models.PROTECT, related_name="children", verbose_name="Родитель", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        full_name = []
        parent = self.parent
        while parent:
            full_name.insert(0, parent.name)
            parent = parent.parent
        if full_name:
            full_name.append(self.name)
            return "->".join(full_name)
        return self.name 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

class Product(models.Model):
    pid = models.CharField(max_length=255, verbose_name="Номер товара")
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-slug")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.00, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    is_available = models.BooleanField(default=True, verbose_name="Наличие")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="categories")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name