FROM python:3.15.0rc1-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app_but_where_is_it

RUN pip install --upgrade pip

COPY DJ-proj/requirements.txt .

RUN pip install -r requirements.txt

COPY DJ-proj/ .

EXPOSE 8000

RUN python manage.py collectstatic --noinput

CMD gunicorn server_side_mySite.wsgi --bind django_test:8000


