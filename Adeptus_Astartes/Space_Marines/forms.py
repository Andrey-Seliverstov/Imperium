from django.forms import ModelForm
from .models import SpaceMarines, Review
from django import forms


class SpaceMarinesForm(ModelForm):
    class Meta:
        model = SpaceMarines
        fields = ['symbol', 'title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'field'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body']

        labels = {
            'body': 'Добавь свой комментарий'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'field'})
