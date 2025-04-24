FROM python:3.12-alpine3.20

ENV PYTHONUNBUFFERED 1

# Instalar las dependencias necesarias (para mysqlclient o pymysql)
RUN apk add --no-cache libffi-dev 

WORKDIR /code

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Ejecutar collectstatic para los archivos estáticos
RUN python manage.py collectstatic --noinput

# Dejar Render manejar el puerto a través de la variable de entorno $PORT
EXPOSE 10000  

# Ejecutar Gunicorn
CMD ["sh", "-c", "gunicorn prueba.wsgi:application --bind 0.0.0.0:${PORT:-10000}", "--timeout", "120", "--workers=1"]
