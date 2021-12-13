from . import models
from django.forms import ModelForm


class BookForm(ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'description', 'image']
