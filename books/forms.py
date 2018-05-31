from django import forms


class AddBookForm(forms.Form):
    title = forms.CharField(label='Title',   max_length=50, required=True)
    author = forms.CharField(label='Author(s)', max_length=50, required=True)
    price = forms.IntegerField(label='Price', required=True)
    btype = forms.ChoiceField(label="Book Type",
               choices=[('h','Hardbound'),('p','Paperbound'), ('d','Digital')])
