from django.shortcuts import render
from django.views import View
from models_app.models.test.models import Test

class ListTestsView1(View):
    def get(self, request):
        tests = Test.objects.all()
        return render(request, 'usu_list_tests.html', {'tests':tests})