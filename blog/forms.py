from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'id_message', 'rows': 5}))