from django import forms


class MailForm(forms.Form):
    name = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)
