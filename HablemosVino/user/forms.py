from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
User= get_user_model()
from user.models import Profile

class SingUpForm(UserCreationForm):

    username = forms.CharField(help_text=None,
                               label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    full_name = forms.CharField(help_text=None,
                               label=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Nombre de completo'}))
    email = forms.EmailField(label=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Correo'}))
    password1 = forms.CharField(label=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña'}))

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
            'password1',
            'password2',
        ]


class LogingForm(AuthenticationForm):
    username = forms.CharField(label=False,
                               help_text=None,
                               widget=forms.TextInput(attrs={'placeholder':'Nombre de usuario'}))

    password = forms.CharField(label=False,
                               help_text=None,
                               widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}))
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

class UserForm(forms.ModelForm):

    username = forms.CharField(help_text=None,
                               label="Nombre de usuario")

    full_name = forms.CharField(help_text=None,
                                label="Nombre Completo")

    email = forms.EmailField(label="Correo")

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email',
        ]

class ProfileForm(forms.ModelForm):

    photo = forms.ImageField(label="Foto",
                             help_text=None,
                             required=False,
                             widget=forms.FileInput())

    twitter = forms.URLField(label="Twitter",
                             help_text=None,
                             required=False
                             )

    linkedin = forms.URLField(label="linkedin",
                             help_text=None,
                             required=False
                              )

    facebook = forms.URLField(label="facebook",
                              help_text=None,
                              required=False
                              )

    twitter = forms.URLField(label="Twitter",
                             help_text=None,
                             required=False,
                             )



    class Meta:
        model = Profile
        fields = [
            'photo',
            'profession',
            'about',
            'birthday',
            'twitter',
            'linkedin',
            'facebook',
        ]

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label=False,
                                   widget=forms.PasswordInput(attrs={'placeholder':'Vieja contraseña'}))
    new_password1 = forms.CharField(label=False,
                                   widget=forms.PasswordInput(attrs={'placeholder': 'Nueva contraseña'}))
    new_password2 = forms.CharField(label=False,
                                   widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))
    class Meta:
        model = User
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]

