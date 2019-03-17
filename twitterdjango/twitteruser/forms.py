from django import forms


class NewUser(forms.Form):
    username = forms.CharField(label='User Name', max_length=15)
    bio = forms.CharField(label='Bio', max_length=200)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    email = forms.CharField(label='Email', widget=forms.EmailInput)


class Login(forms.Form):
    username = forms.CharField(label="Username", max_length=15)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
