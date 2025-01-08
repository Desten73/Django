from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, label="Введите ваше имя:")
    password = forms.CharField(label="Введите ваш пароль:")
    repeat_password = forms.CharField(label="Повторите ваш пароль:")
    email = forms.EmailField(label="Введите вашу почту:")
    age = forms.IntegerField(label="Введите ваш возраст:")
    agreement = forms.BooleanField(label="Согласие на обработку персональных данных")
