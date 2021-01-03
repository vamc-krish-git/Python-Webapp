FROM python:3.9.0
WORKDIR /code
ENV FLASK_APP=app.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
COPY . .
CMD ["flask", "run"]