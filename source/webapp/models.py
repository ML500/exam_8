from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = [
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Продукты питания'),
    ('household', 'Хоз. товары'),
    ('toys', 'Детские игрушки'),
    ('appliances', 'Бытовая Техника')
]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.TextField(max_length=20, choices=CATEGORY_CHOICES,
                                default=DEFAULT_CATEGORY, verbose_name='Категория')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Картинка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews',
                               verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='reviews',
                                on_delete=models.CASCADE, verbose_name='Товар')
    text_review = models.TextField(max_length=2000, verbose_name='Текст отзыва')
    rating = models.IntegerField(verbose_name='Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.author} - {self.product}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
