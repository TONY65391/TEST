from django import forms
from . models import UserProfile

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter your full name'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email address'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Create a password'})
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter password'})
        