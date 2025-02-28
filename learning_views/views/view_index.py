"""    index на классах (на обычных, без ListView, DetailView, UpdateView ...)  """

"""
    Вывод через class MyView(View)
    JsonResponse В Шаблоне НЕ ЛОВИТЬ!
"""

# from django.http import JsonResponse
# from django.views import View
#
# class MyView(View):
#     def get(self, request):
#         data = {"message": "Hello Art from Class-Based View"}
#         return JsonResponse(data)


"""
    Вывод через class MyView(View)
    HttpResponse В Шаблоне НЕ ЛОВИТЬ!
"""
# # Вывод через class MyView(View)-HttpResponse В Шаблоне НЕ ЛОВИТЬ!
# from django.http import HttpResponse
# from django.views import View
#
# class MyView(View):
#     def get(self, request):
#         return HttpResponse("Hello Art, this is HttpResponse")

"""
    Вывод через class MyView(View)
    render В этом варианте, я ловлю переменную "x" в html-шаблоне
"""

from django.shortcuts import render
from django.views import View

class MyView(View):
    def get(self, request):
        context = {
            "x": "Hello Art class",
            "y": "This is a normal index from render, from class MyView(View)"
        }
        return render(request, "index.html", context)