FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY application.py .

EXPOSE 9191

CMD [ "gunicorn",  "-b",  "0.0.0.0:9191", "application:app"]



