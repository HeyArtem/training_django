from django.shortcuts import get_object_or_404, redirect, render
from models_app.models.test.models import Test

def delete_test(request, slug):
    test = get_object_or_404(Test, slug=slug)

    if request.method == "POST":
        test.delete()
        return redirect("list_tests")  # Редирект на список тестов

    return render(request, "fn_delete_test.html", {"test": test})
