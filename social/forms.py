from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, ExtendedData
from django.contrib.auth.forms import UserChangeForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    pregunta_seguridad = forms.ChoiceField(choices=Profile.SECURITY_QUESTION_CHOICES, label='Pregunta de seguridad')
    respuesta_seguridad = forms.CharField(max_length=100, label='Respuesta de seguridad')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'pregunta_seguridad', 'respuesta_seguridad']
        help_texts = {k: "" for k in fields}

class PostForm(forms.ModelForm):
    content=forms.CharField(label='',widget=forms.Textarea(attrs={'rows':2,'placeholder':'Agrega una descripción de tu obra'}),required=True)
    post_title = forms.CharField(label='Título', required=True)
    picture = forms.ImageField(label='Imagen', required=True)

    class Meta:
        model=Post
        fields=['post_title', 'content', 'picture']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = ExtendedData
        fields = ["user_type"]

class EditProfileForm(forms.ModelForm):
    description = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'rows': 4}), required=False)

    class Meta:
        model = User
        fields = ['username', 'email']


class SecurityQuestionForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', required=True)
    pregunta_seguridad = forms.CharField(label='Pregunta de seguridad', required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    respuesta_seguridad = forms.CharField(max_length=100, label='Respuesta de seguridad', required=False)

    def set_security_question(self, pregunta, respuesta):
        self.fields['pregunta_seguridad'].initial = pregunta
        self.fields['respuesta_seguridad'].initial = respuesta

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario no existe.')
        return username


class PasswordResetForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    new_password = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)

