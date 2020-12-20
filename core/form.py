from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')
    first_name = forms.CharField(max_length=254, help_text='Это поле обязательно')
    second_name = forms.CharField(max_length=254, help_text='Это поле обязательно')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'email', 'first_name', 'second_name',)

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return self.cleaned_data
