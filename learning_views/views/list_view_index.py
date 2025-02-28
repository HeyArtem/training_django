"""
    ListView – вывод списка объектов
    Используется, когда нужно вывести сразу несколько объектов (например, список тестов).
"""
from django.views.generic import ListView
from models_app.models.test.models import Test

class ListTestsView(ListView):
    model = Test
    template_name = "list_tests.html"
    context_object_name = "tests"

