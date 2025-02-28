from django import forms
from models_app.models.test.models import Test

class TestForm(forms.ModelForm):
    """
        Форма используется при создании теста
        в fn_create_test.py
    """
    class Meta:
        model = Test
        fields = ['title', 'category', 'description', 'is_published', 'cover']
