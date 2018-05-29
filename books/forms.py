from django import forms


class AddBookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50, required=True)
    author = forms.CharField(label='Author', max_length=50, required=True)
    price = forms.IntegerField(label='Price', required=True)
