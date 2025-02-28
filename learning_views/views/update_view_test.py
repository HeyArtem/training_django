from django.views.generic import UpdateView
from models_app.models.test.models import Test
from django.urls import reverse_lazy

class UpdateTestView(UpdateView):
    model = Test
    fields = [
        "title",
        "category",
        "description",
        "slug"
    ]
    template_name = "update_test.html"

# todo а как еще можно перенаправить и если нет slug???
    def get_success_url(self):
        return reverse_lazy("retrieve_test_view", kwargs={"slug": self.object.slug})

