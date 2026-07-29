# for login register logout.
# 2.0
# from django import forms
#
# class LoginForm(forms.Form):
#     phone = forms.CharField(label="Telefon raqam", max_length=13)
#     password = forms.CharField(label="Parol", widget=forms.PasswordInput)
#
#
# class RegisterForm(forms.Form):
#     first_name = forms.CharField(label="Ism", max_length=100)
#     last_name = forms.CharField(label="Familiya", max_length=100, required=False)
#     phone = forms.CharField(label="Telefon raqam", max_length=13)
#     email = forms.EmailField(label="Email")
#     password = forms.CharField(label="Parol", widget=forms.PasswordInput)


# Profil uchun.
# 3.0
# from django import forms
# from .models import CustomUser
#
# class LoginForm(forms.Form):
#     phone = forms.CharField(label="Telefon raqam", max_length=13)
#     password = forms.CharField(label="Parol", widget=forms.PasswordInput)
#
#
# class RegisterForm(forms.Form):
#     first_name = forms.CharField(label="Ism", max_length=100)
#     last_name = forms.CharField(label="Familiya", max_length=100, required=False)
#     phone = forms.CharField(label="Telefon raqam", max_length=13)
#     email = forms.EmailField(label="Email")
#     password = forms.CharField(label="Parol", widget=forms.PasswordInput)
#
#
# class ProfileForm(forms.ModelForm):
#     GENDER_CHOICES = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     ]
#     gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label="Jinsi")
#
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email', 'phone', 'passport', 'birth_date', 'gender']
#         widgets = {
#             'birth_date': forms.DateInput(attrs={'type': 'date'}),
#         }


# Parolni o'zgartirish, yangilash, esdan chiqqanda o'zgartirish va validatsiya.
# 4.0
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser


def validate_password_length(password):
    if len(password) < 8 or len(password) > 32:
        raise ValidationError("Parol kamida 8, ko'pi bilan 32 belgidan iborat bo'lishi kerak.")


class LoginForm(forms.Form):
    phone = forms.CharField(label="Telefon raqam", max_length=13)
    password = forms.CharField(label="Parol", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="Ism", max_length=100)
    last_name = forms.CharField(label="Familiya", max_length=100, required=False)
    phone = forms.CharField(label="Telefon raqam", max_length=13)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Parolni tasdiqlang", widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password_length(password)
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Parollar bir-biriga mos kelmadi.")
        return cleaned_data


class ProfileForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label="Jinsi")

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'passport', 'birth_date', 'gender']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label="Eski parol", widget=forms.PasswordInput)
    new_password = forms.CharField(label="Yangi parol", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Yangi parolni tasdiqlang", widget=forms.PasswordInput)

    def clean_new_password(self):
        password = self.cleaned_data['new_password']
        validate_password_length(password)
        return password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        if new_password and confirm_password and new_password != confirm_password:
            raise ValidationError("Yangi parollar bir-biriga mos kelmadi.")
        return cleaned_data


class ForgotPasswordIdentifyForm(forms.Form):
    identifier = forms.CharField(label="Telefon raqam yoki Email")


class SetNewPasswordForm(forms.Form):
    new_password = forms.CharField(label="Yangi parol", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Yangi parolni tasdiqlang", widget=forms.PasswordInput)

    def clean_new_password(self):
        password = self.cleaned_data['new_password']
        validate_password_length(password)
        return password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        if new_password and confirm_password and new_password != confirm_password:
            raise ValidationError("Parollar bir-biriga mos kelmadi.")
        return cleaned_data