from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=100,
                               widget=forms.TextInput(attrs={'id': 'username'}))
    password = forms.CharField(label='Пароль', max_length=100,
                               widget=forms.PasswordInput(attrs={'id': 'password'}))
    # email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'id': 'email'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=100,
                               widget=forms.TextInput(attrs={'id': 'login'}))

    first_name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={'id': 'username'}))

    password1 = forms.CharField(label='Пароль', max_length=100,
                               widget=forms.PasswordInput(attrs={'id': 'password'}))

    password2 = forms.CharField(label='Повтор пароля', max_length=100,
                                widget=forms.PasswordInput(attrs={'id': 'password'}))

    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'id': 'email'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'username', 'email', 'password1', 'password2')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Пароли не совпадают')
    #     return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такая электронная почта уже зарегистрирована')
        return email

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if get_user_model().objects.filter(username=username).exists():
    #         raise forms.ValidationError('Такой логин уже существует')
    #     return username
