from django.contrib import admin
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Usuario

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['email', 'get_full_name', 'rut', 'estado_verificacion', 'fecha_registro']
    list_filter = ['estado_verificacion', 'fecha_registro']
    search_fields = ['email', 'first_name', 'apellido_paterno', 'apellido_materno', 'rut']
    readonly_fields = ['fecha_registro']
    fieldsets = (
        ('Información Personal', {
            'fields': (
                'email', 'first_name', 'apellido_paterno', 'apellido_materno',
                'rut', 'numero_documento', 'direccion', 'telefono'
            )
        }),
        ('Documentos', {
            'fields': ('foto_perfil', 'foto_carnet_frente', 'foto_carnet_dorso')
        }),
        ('Estado de Verificación', {
            'fields': ('estado_verificacion', 'fecha_verificacion', 'notas_verificacion')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    def save_model(self, request, obj, form, change):
        if change and 'estado_verificacion' in form.changed_data:
            # Determinar la plantilla y asunto según el estado
            templates = {
                'verificado': ('verificacion_aprobada.html', '¡Tu cuenta ha sido aprobada!'),
                'rechazado': ('verificacion_rechazada.html', 'Verificación de cuenta no aprobada'),
                'pendiente': ('verificacion_pendiente.html', 'Actualización de estado de verificación'),
                'en_proceso': ('verificacion_pendiente.html', 'Actualización de estado de verificación'),
            }
            
            template_name, subject = templates.get(obj.estado_verificacion, 
                                                 ('verificacion_pendiente.html', 'Actualización de estado de verificación'))
            
            # Renderizar el correo
            html_message = render_to_string(f'usuarios/email/{template_name}', {
                'user': obj,
            })
            plain_message = strip_tags(html_message)
            
            # Enviar el correo
            send_mail(
                subject,
                plain_message,
                'noreply@goworq.com',
                [obj.email],
                html_message=html_message,
                fail_silently=False,
            )
            
            # Actualizar fecha de verificación
            obj.fecha_verificacion = timezone.now()
            obj.verificado_por = request.user
            
        super().save_model(request, obj, form, change)
