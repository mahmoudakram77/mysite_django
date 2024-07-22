from django import forms



class loginForm(forms.Form):
  username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
  password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))