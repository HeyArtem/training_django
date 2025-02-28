from django.shortcuts import render, redirect
from django.views import View
from learning_views.forms import TestForm


class CreateTestView1(View):
    def get(self, request):
        """ рендерит пустую форму """
        form = TestForm()
        return render(request, 'usu_create_test.html', {'form':form})

    def post(self, request):
        """ проверяет данные, сохраняет тест и перенаправляет """
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('usu_list')
        return render(request, 'usu_create_test.html', {'form':form})
