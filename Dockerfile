FROM python:3.12-alpine3.20 

ENV PYTHONUNBUFFERED 1

# Agrega mariadb-connector-c-dev en lugar de postgresql-dev
RUN apk add --no-cache gcc musl-dev mariadb-connector-c-dev

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "prueba.wsgi:application", "--bind", "0.0.0.0:8000"]
