""" FBN вывод одного теста """

from django.shortcuts import render, get_object_or_404
from models_app.models.test.models import Test

def retrive_test(request, slug):
    test = get_object_or_404(Test, slug=slug)
    return render(request, template_name="fn_retrieve_test.html", context={"test":test})