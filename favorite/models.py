from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Favorite(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    specialist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_specialists')

    class Meta:
        verbose_name = "Избранный специалист"
        verbose_name_plural = "Избранные специалисты"
