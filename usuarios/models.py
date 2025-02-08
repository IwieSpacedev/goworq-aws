from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(AbstractUser):
    ESTADO_VERIFICACION = (
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('verificado', 'Verificado'),
        ('rechazado', 'Rechazado')
    )

    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    rut = models.CharField(max_length=20)
    numero_documento = models.CharField(max_length=20)
    direccion = models.TextField()
    foto_perfil = models.ImageField(upload_to='fotos_perfil/')
    foto_carnet_frente = models.ImageField(upload_to='fotos_carnet/')
    foto_carnet_dorso = models.ImageField(upload_to='fotos_carnet/')
    telefono = models.CharField(max_length=20)
    estado_verificacion = models.CharField(
        max_length=20,
        choices=ESTADO_VERIFICACION,
        default='pendiente'
    )
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_verificacion = models.DateTimeField(null=True, blank=True)
    verificado_por = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='verificaciones'
    )
    notas_verificacion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_full_name(self):
        return f"{self.first_name} {self.apellido_paterno} {self.apellido_materno}"
