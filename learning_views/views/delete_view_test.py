from django.views.generic import DeleteView
from models_app.models.test.models import Test
from django.urls import reverse_lazy

class DeleteTestView(DeleteView):
    model = Test
    template_name = "delete_test.html"
    success_url = reverse_lazy("generic_index")