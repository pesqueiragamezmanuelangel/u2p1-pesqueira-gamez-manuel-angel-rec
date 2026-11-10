
Escribir el README
README.md
<!-- título del repo: cambia por tus nombres reales -->
# U2S3 — Pesqueira Gamez Manuel Angel

<!-- sección con los pasos para correr el proyecto en otra computadora -->
## Cómo correrlo localmente
<!-- paso 1: el entorno virtual -->
1. Crear y activar un entorno virtual
<!-- paso 2: instalar los paquetes de requirements.txt -->
2. pip install -r requirements.txt
<!-- paso 3: crear el .env a partir del ejemplo -->
3. Copiar .env.example a .env y completar con credenciales propias de Aiven
<!-- paso 4: crear las tablas en MySQL -->
4. python manage.py migrate
<!-- paso 5: arrancar el servidor -->
5. python manage.py runserver

<!-- sección con la evidencia de la práctica -->
## Evidencia
<!-- dónde están las capturas -->
Ver capturas de `migrate` y de las tablas en Aiven en la carpeta /evidencias.