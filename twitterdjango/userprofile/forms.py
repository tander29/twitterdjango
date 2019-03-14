from django import forms


class NewUser(forms.Form):
    displayname = forms.CharField(label='Display Name', max_length=15)
    date_created = forms.TimeField()
    bio = forms.CharField(label='Bio', max_length=200)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    email = forms.CharField(label='Email', widget=forms.EmailInput)
