from django import forms

messages ={
    'required':'invalid field'
}

class UserLoginForm(forms.Form):
    username = forms.CharField(error_messages=messages,max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(max_length=40,
                              widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

class UserRegisterationForm(forms.Form):
    username = forms.CharField(error_messages=messages,max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(error_messages=messages,max_length=40,
                              widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    email = forms.EmailField(error_messages=messages,max_length=50,
                             widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'email'}))