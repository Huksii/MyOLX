from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

CATEGORY_CHOICES = (
    ('real_estate', 'Недвижимость'),
    ('transport', 'Транспорт'),
    ('home_and_garden', 'Товары для дома и сада'),
    ('electronics', 'Электроника'),
    ('clothing_and_footwear', 'Одежда и обувь'),
    ('services', 'Услуги'),
    ('pets', 'Животные'),
    ('sports_and_hobbies', 'Спорт и хобби'),
    ('business_and_equipment', 'Бизнес и оборудование'),
    ('food_and_drinks', 'Продукты и напитки'),
)

class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Названия",
        help_text="Название категории, например, 'Недвижимость' или 'Транспорт'",
        unique=True
    )
    main_category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        verbose_name="Родительская категория",
        help_text="Родительская категория(если есть)",
        default='real_estate'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания этой категории",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Ads(models.Model):
    image = models.ImageField(
        upload_to='ads_images/',
        verbose_name="Изображение",
        help_text="Изображение, связанное с объявлением",
    )

    title = models.CharField(
        max_length=100,
        verbose_name="Название",
        help_text="Заголовок объявления, например, 'Продам ноутбук ASUS XPS'",
    )
    
    description = models.TextField(
        verbose_name="Описание",
        max_length=999,
        help_text="Подробное описание объявления, включая характеристики и детали",
    )
    
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Цена товара или услуги, например, '1500.00'",
    )
    
    def validator_price(value):
        if value.price < 0:
            raise ValidationError("Цена не может быть меньше 0")
        return value.price
    
    contact = models.CharField(
        max_length=100,
        verbose_name="Телефон для связи",
        help_text="Контактный телефон для связи с автором объявления",
    )
    
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank=True,
        null=True,
        help_text="Физический адрес, если применимо",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Категория, к которой принадлежит объявление",
    )
    
    whatsapp = models.URLField(
        verbose_name="Ссылка на whatsapp",
        blank=True,
        null=True,
        help_text="Ссылка на WhatsApp для связи с автором объявления",
    )
    
    telegram = models.URLField(
        verbose_name="Ссылка на telegram",
        blank=True,
        null=True,
        help_text="Ссылка на Telegram для связи с автором объявления",
    )
    
    instagram = models.URLField(
        verbose_name="Ссылка на instagram",
        blank=True,
        null=True,
        help_text="Ссылка на Instagram для связи с автором объявления",
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Пользователь, который разместил объявление",
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания объявления",
    )

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"