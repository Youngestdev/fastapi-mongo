FROM python:3.8

ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.server.app:app", "--host", "0.0.0.0", "--port", "80"]
