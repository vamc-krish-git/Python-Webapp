FROM python:3.9.0
WORKDIR /code
COPY run.sh ./

# Start and enable SSH
RUN apt-get update \
    && apt-get install -y --no-install-recommends dialog \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd \
    && chmod u+x /code/run.sh
COPY sshd_config /etc/ssh/
ENV FLASK_APP=app.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 3000 2222
COPY . .
ENTRYPOINT ["sh","/code/run.sh"]
