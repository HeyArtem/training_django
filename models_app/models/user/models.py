from django.contrib.auth.models import AbstractUser
from django.db import models

"""
❗️когда переопределяешь модель пользователя, нужно прописать  в сеттингах
        AUTH_USER_MODEL = "models_app.User"        
"""
class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="users/avatar/", null=True, blank=True, verbose_name="Аватар"
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
