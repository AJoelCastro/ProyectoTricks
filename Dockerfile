FROM python:3.12-alpine3.20 

ENV PYTHONUNBUFFERED 1

# Instalar las dependencias del sistema necesarias para mysqlclient
RUN apk add --no-cache gcc musl-dev mariadb-dev

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "check"]

