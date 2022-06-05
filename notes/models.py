from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name='Заметка')
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    importance = models.BooleanField(default=False, verbose_name='Важность')
    create_date = models.DateTimeField(default=timezone.now(), verbose_name='Время создания')
    complete = models.BooleanField(default=False, verbose_name='Выполнено')
    complete_date = models.DateTimeField(default=timezone.now() + timedelta(days=1), verbose_name='Время выполнения')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    class Choices(models.TextChoices):
        ACTIVE = "Активно"
        POSTPONE = "Отложено"
        COMPLETE = "Выполнено"
    status = models.CharField(max_length=10, choices=Choices.choices, default=Choices.ACTIVE, verbose_name='Статус')

    def __str__(self):
        return self.title