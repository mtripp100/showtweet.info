FROM kennethreitz/pipenv

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "2", "showtweet:app"]
