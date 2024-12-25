from django.forms import ModelForm
from .models import History
from django import forms


class HistoryForm(ModelForm):
    class Meta:
        model = History
        fields = ['millennium', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'field'})
