from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение', upload_to='post_images/', blank=True, null=True)  
    view_count = models.IntegerField(verbose_name='Кол-во просмотров', default=0)

    def __str__(self):
        return self.title