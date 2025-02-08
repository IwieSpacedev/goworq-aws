from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import RegistroUsuarioForm
from .models import Usuario

# Create your views here.

class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/inicio.html'
    login_url = 'login'

class LoginUsuarioView(LoginView):
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return self.success_url

class RegistroUsuarioView(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        # Enviar correo de bienvenida
        subject = '¡Bienvenido a GoworQ! Verificaremos tu cuenta pronto'
        html_message = render_to_string('usuarios/email/bienvenida.html', {
            'user': user,
        })
        plain_message = strip_tags(html_message)
        
        send_mail(
            subject,
            plain_message,
            'noreply@goworq.com',
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        return redirect(self.success_url)

class LogoutUsuarioView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
