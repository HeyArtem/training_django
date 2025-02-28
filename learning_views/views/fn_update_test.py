from django.shortcuts import get_object_or_404, redirect, render
from models_app.models.test.models import Test
from learning_views.forms import TestForm


# def update_test(request, id):
def update_test(request, slug):
    test = get_object_or_404(Test, slug=slug)

    if request.method == "POST":
        """
        instance=test, Django не создаст новый объект, а обновит существующий.
        Если не передавать instance, Django подумает, что создаётся новый объект.
        """
        form = TestForm(request.POST, instance=test)    # Форма заполняется данными test
        if form.is_valid():
            form.save()
            return redirect("fn_test", slug=test.slug)  # Редирект на детальный просмотр
    else:
        # рендерим форму с заполненными данными.
        form = TestForm(instance=test)

    return render(request, "fn_update_test.html", {"form": form, "test": test})