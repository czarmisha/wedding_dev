from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Budget(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE, related_name='budget', unique=True)
    budget_json = models.JSONField(blank=True)
    budget_value = models.FloatField('Сумма бюджета', default=0)
    last_rel = models.IntegerField(default=80)

    class Meta:
        verbose_name = 'Свадебный Бюджет'
