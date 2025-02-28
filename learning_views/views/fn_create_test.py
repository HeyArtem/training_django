from django.shortcuts import render, redirect
from models_app.models.test.models import Test
from learning_views.forms import TestForm


def create_test(request):
    """
        Создание теста
        (slug-создается автоматич. в def generate_unique_slug(self):)

        request.FILES — это словарь загруженных файлов (Если в форме есть файл
        (например, картинка), он не передаётся через request.POST,
        а идёт отдельно через request.FILES.). html-Форма должна содержать enctype="multipart/form-data", иначе файлы не передаются!
    """
    if request.method == "POST":
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user  # Привязываем автора
            form.save()
            return redirect("fn_list")  # Перенаправление на список тестов
    else:
        form = TestForm()

    return render(request, "fn_create_test.html", {"form": form})
