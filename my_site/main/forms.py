from .models import Reader
from django.forms import ModelForm, TextInput, Select


class ReaderForm(ModelForm):
    class Meta:
        model = Reader
        fields = ['name', 'gender']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'gender': Select()
        }