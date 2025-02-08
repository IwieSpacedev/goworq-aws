from django.urls import path
from .views import LoginUsuarioView, RegistroUsuarioView, InicioView, LogoutUsuarioView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('logout/', LogoutUsuarioView.as_view(), name='logout'),
]
