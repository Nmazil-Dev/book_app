from django import forms
from .models import Book
from django.forms import ModelForm


class NameForm(forms.Form):
    book_search = forms.CharField(label='Enter Book', max_length=100)

class PageForm(ModelForm):
    class Meta:
        model = Book
        fields = ['current_page']
