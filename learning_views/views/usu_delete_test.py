from django.template.context_processors import request
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from models_app.models.test.models import Test


class DeleteTestView1(View):
    def get(self, request, slug):
        test = get_object_or_404(Test, slug=slug)
        return render(request, 'usu_delete_test.html', {'test':test})

    def post(self, request, slug):
        test = get_object_or_404(Test, slug=slug)
        test.delete()
        return redirect('usu_list')