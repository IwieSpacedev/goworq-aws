import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'goworq.settings')
django.setup()

from usuarios.models import Usuario

def create_superuser():
    if not Usuario.objects.filter(username='admin').exists():
        Usuario.objects.create_superuser(
            username='admin',
            email='admin@goworq.com',
            password='admin123',
            first_name='Admin',
            apellido_paterno='Sistema',
            apellido_materno='GoWorq',
            rut='00000000-0',
            numero_documento='00000000',
            direccion='Dirección Admin',
            telefono='000000000'
        )
        print("Superusuario creado exitosamente")
    else:
        print("El superusuario ya existe")

if __name__ == '__main__':
    create_superuser()
