from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nombre'
    )
    apellido_paterno = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    apellido_materno = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    rut = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    numero_documento = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    foto_perfil = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    foto_carnet_frente = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    foto_carnet_dorso = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    telefono = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validate_password]
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuario
        fields = [
            'email', 'password1', 'password2',
            'first_name', 'apellido_paterno', 'apellido_materno',
            'rut', 'numero_documento', 'direccion',
            'foto_perfil', 'foto_carnet_frente',
            'foto_carnet_dorso', 'telefono'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
