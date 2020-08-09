from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="название товара"
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="краткое описание"
    )
    image_main = models.ImageField(
        null=True,
        blank=True,
        upload_to="product_image",
        verbose_name="основное изображение товара",
        default="static/no_image.png"
    )
    images_additional = models.ImageField(
        null=True,
        blank=True,
        upload_to="product_images",
        verbose_name="дополнительные изображения товара"
    )
    price_new = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2,
        verbose_name="новая цена"
    )
    price_old = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2,
        verbose_name="старая цена"
    )
    tag = models.CharField(
        max_length=50,
        verbose_name="тэг"
    )
    sku =  models.IntegerField(
        default=0,
        verbose_name="номер товара"
    )
    quantity_purchases = models.IntegerField(
        default=0,
        verbose_name="колличество в магазине"
    )
    availability_in_store = models.BooleanField(
        default=True,
        verbose_name="наличие в магазине"
    )
    introduction = models.CharField(
        max_length=255,
        verbose_name="полное описание"
    )
    features = models.CharField(
        max_length=255,
        verbose_name="характеристики"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["name"]


class Parametr(models.Moldel):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="категория"
    )
    color = ColorField(
        default='#FF0000'
    )
    size = models.CharField(
        max_length=10,
        verbose_name="название"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Параметр"
        verbose_name_plural = "Параметры"


class Brand(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="категория"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренд"


class Category(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="категория"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

class Customer(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="product",
        verbose_name="Покупатель"
    )
    likes = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="категория"
    )
    card = 