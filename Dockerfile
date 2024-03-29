FROM python:3.11.0a4-slim-buster

ADD . ./app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]