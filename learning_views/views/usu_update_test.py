from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from learning_views.forms import TestForm
from models_app.models.test.models import Test


class UpdateTestView1(View):
    """
        В View-классах Django сам вызывает нужный метод (get() или post()),
        в зависимости от запроса (только в функциях if request.method == "POST"..).
    """
    def get(self, request, slug):
        test = get_object_or_404(Test, slug=slug)
        form = TestForm(instance=test)
        return render(request, 'usu_update_test.html', {'test':test, 'form':form})

    def post(self, request, slug):
        test = get_object_or_404(Test, slug=slug)
        form = TestForm(request.POST, request.FILES, instance=test)
        if form.is_valid():
            form.save()
            return redirect('usu_retrive', slug=slug)
        return render(request, 'usu_update_test.html', {'form':form, 'test':test})
