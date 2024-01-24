from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import User


class Project(models.Model):
    CHOICES = [
        ('electronucs', 'Электроника'),
        ('food', 'Еда')
    ]
    title = models.CharField(max_length=50, verbose_name='Название')
    category = models.CharField(max_length=50, choices=CHOICES, verbose_name='Категория')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(upload_to='project_pictures', null=True, blank=True, verbose_name='Картинка')

    def __str__(self):
        return f'{self.title}({self.id})'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews', verbose_name='Продукт')
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Оценка')
    moderated = models.BooleanField(default=False, verbose_name='Промоделированный')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'({self.id}){self.author} - {self.text}'