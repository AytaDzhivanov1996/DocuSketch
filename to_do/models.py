from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Task(models.Model):
    """Модель задачи"""
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания задачи')
    file = models.FileField(upload_to='mdeia/', verbose_name='Файл', **NULLABLE)