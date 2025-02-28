"""  FBN, вывожу все тесты  """

from django.shortcuts import render
from models_app.models.test.models import Test

def list_tests(request):
    tests = Test.objects.all()
    return render(request, template_name="fn_list_tests.html", context={'tests':tests})
