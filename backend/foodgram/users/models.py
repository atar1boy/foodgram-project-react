from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя.
    """
    email = models.EmailField(
        'Электронная почта пользователя',
        unique=True,
        max_length=254,
    )
    first_name = models.CharField(
        'Имя пользователя',
        max_length=150,
    )
    last_name = models.CharField(
        'Фамилия пользователя',
        max_length=150,
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email


class Subscription(models.Model):
    """
    Модель Подписок пользователей.
    """
    user = models.ForeignKey(
        CustomUser,
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
        related_name='follower',
    )
    author = models.ForeignKey(
        CustomUser,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscription'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} подписан на {self.author}'
