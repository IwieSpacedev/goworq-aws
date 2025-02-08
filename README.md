# Goworq

Una aplicación Django para gestión de tareas.

## Requisitos

- Python 3.x
- PostgreSQL
- pip

## Instalación

1. Clonar el repositorio:
```bash
git clone <tu-repositorio>
cd goworq
```

2. Crear un entorno virtual e instalar dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configurar variables de entorno:

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
```
DJANGO_SECRET_KEY=tu_clave_secreta
DJANGO_DEBUG=True
DB_NAME=goworq
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=tu_host
DB_PORT=5432
```

4. Ejecutar migraciones:
```bash
python manage.py migrate
```

5. Ejecutar el servidor de desarrollo:
```bash
python manage.py runserver
```

## Despliegue

### AWS Elastic Beanstalk

La aplicación está configurada para desplegarse en AWS Elastic Beanstalk. Los archivos de configuración necesarios están en el directorio `.ebextensions/`.

Para desplegar:
1. Crear un entorno en Elastic Beanstalk con Python
2. Configurar las variables de entorno en la consola de Elastic Beanstalk
3. Subir el código como archivo zip

### Variables de Entorno Requeridas

- `DJANGO_SECRET_KEY`: Clave secreta de Django
- `DJANGO_DEBUG`: 'True' o 'False'
- `DJANGO_ALLOWED_HOSTS`: Lista de hosts permitidos separados por comas
- `DB_NAME`: Nombre de la base de datos
- `DB_USER`: Usuario de la base de datos
- `DB_PASSWORD`: Contraseña de la base de datos
- `DB_HOST`: Host de la base de datos
- `DB_PORT`: Puerto de la base de datos (por defecto: 5432)
