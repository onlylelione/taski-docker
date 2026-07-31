"""Конфигурация приложения API для проекта."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Конфигурация Django‑приложения для API."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
