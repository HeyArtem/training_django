from django.shortcuts import render, get_object_or_404
from django.views import View
from models_app.models.test.models import Test

class RetriveTestView1(View):
    def get(self, request, slug):
        test = get_object_or_404(Test, slug=slug)
        return render(request, 'usu_retrieve_test.html', {'test':test})