"""
    JsonResponse
    Используется, когда нужно вернуть данные в формате JSON (например, для API, AJAX-запросы, работа с фронтом).
    html - НЕ НУЖЕН !!!
"""

# from django.http import JsonResponse
#
# def idex(request):
#     data = {"message": "Hello Art"}
#     return JsonResponse(data)

# """
#     Этот вариант просто возвращает текст в браузер.
#     html - НЕ НУЖЕН !!!
# """
#
# from django.http import HttpResponse
#
# def idex(request):
#     return HttpResponse("Hello Art from HttpResponse")

"""
    Классические Django-шаблоны (HTML)
    Полная поддержка контекста, стилей, шаблонов
"""


from django.shortcuts import render

def index(request):
    context = {
        "x": "Hello Art func",
        "y": "This is a normal index from render"
    }
    return render(request, "fn_index.html", context)

"""
    📌 Используются ли?
    * HttpResponse – редко, в основном для быстрых тестов или при отдаче простого текста.
    * JsonResponse – активно используется в API (Django REST Framework, AJAX-запросы).
    * render (шаблон) – основной способ для отображения страниц на Django.
"""