FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code

RUN pip install poetry

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]