from django import forms
from django.forms.widgets import TextInput

class SearchInput(TextInput):
    input_type = 'search'

class SearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=255,
        widget=SearchInput
    )
