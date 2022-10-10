from django.db import models
from django import forms


class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Description')

    def __str__(self):
        return self.title


GENDER_CHOICES = (
    ('M', 'Муж.'),
    ('F', 'Жен.')
)


class Reader(models.Model):
    name = models.CharField('Name', max_length=30)
    gender = models.CharField('Gender', max_length=10, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return self.name


class Post(models.Model):
    text = models.TextField(
        'Текст поста',
        help_text='Введите текст поста'
    )

    image = models.ImageField(
        'Image',
        upload_to='img/',
        blank=True
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:15]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image')
