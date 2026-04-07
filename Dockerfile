FROM python:3.15.0a7-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app_but_where_is_it

RUN pip install --upgrade pip

COPY DJ-proj/requirements.txt .

RUN pip install -r requirements.txt

COPY DJ-proj/ .

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
