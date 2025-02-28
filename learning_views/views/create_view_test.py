"""
    CreateView – создание нового объекта
    Используется, когда нужно создать новый объект через форму.
"""

from django.views.generic import CreateView
from models_app.models.test.models import Test
from django.urls import reverse_lazy

class CreateTestView(CreateView):
    model = Test
    fields = [
        "title",
        "category",
        "description",
        "slug",
        "author",
    ]
    template_name = "create_test.html"
    # Перенаправление при успехе
    success_url = reverse_lazy("generic_index")

# todo Как картинку подгружать???

"""
    reverse_lazy() откладывает вычисление URL до момента, когда он реально понадобится. 
    Это полезно в CreateView, UpdateView, DeleteView, потому что Django сначала загружает код вьюхи, 
    а потом уже обрабатывает URL-ы.
    Какие ещё есть варианты?
    ✅ reverse() – вычисляет URL сразу (не откладывает, как reverse_lazy).
"""