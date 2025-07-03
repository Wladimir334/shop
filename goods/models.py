from django.db import models
from django.db.models import CASCADE


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200, unique=True,  verbose_name='Название')
    slug = models.SlugField(max_length=300, unique=True, blank=True, null=True, verbose_name='URL_Product')
    description = models.TextField(verbose_name='Описание товара', blank=True, null=True)
    image = models.ImageField(upload_to="Product_image/%Y/%m/%d", default='default.jpg' ,verbose_name='Изображение', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id',)

    def __str__(self):
        return self.name



