FROM python:3.12-alpine3.20

ENV PYTHONUNBUFFERED 1

# Instalar las dependencias del sistema necesarias para mysqlclient
#esto para mysqlclient
#RUN apk add --no-cache gcc musl-dev mariadb-dev 
#aqui para pymysql
RUN apk add --no-cache libffi-dev 

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["sh", "-c", "gunicorn prueba.wsgi:application --bind 0.0.0.0:${PORT:-10000}", "--timeout", "120","--workers=1"]



