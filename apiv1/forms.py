from django import forms

class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)