from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    time = models.TimeField('Время')
    action = models.TextField('Описание', max_length=255)


