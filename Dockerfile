FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code

RUN pip install poetry
RUN poetry install --no-root

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]