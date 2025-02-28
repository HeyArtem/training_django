"""
    DetailView – вывод одного объекта
    Используется, когда нужно отобразить один конкретный объект из БД.
"""

from django.views.generic import DetailView
from models_app.models.test.models import Test  # Импортируем модель

class RetrieveTestView(DetailView):
    model = Test
    template_name = "retrieve_test.html"
    context_object_name = "test"