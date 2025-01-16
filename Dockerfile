FROM python:3.12-alpine3.20 

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache postgresql-dev gcc musl-dev

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]