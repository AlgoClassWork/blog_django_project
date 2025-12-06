from django.db import models
from django.urls import reverse

class Game(models.Model):
    title = models.CharField('Название', max_length=200)
    genre = models.CharField('Жанр', max_length=100)
    release_year = models.PositiveIntegerField('Год название')
    description = models.TextField('Описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'pk': self.pk})