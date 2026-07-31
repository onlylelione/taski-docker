"""Сериализаторы для проекта."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Настройки сериализатора для модели Task."""

    class Meta:
        """Настройки сериализатора для модели Task."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
