FROM python:3.12-alpine3.20 

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache postgresql-dev gcc musl-dev

RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

CMD ["gunicorn","-c","config/gunicorn/conf.py", "--bind",":8000", "--chdir", "prueba", "prueba.wsgi:application"]