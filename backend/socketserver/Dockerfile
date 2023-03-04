# Dockerfile
FROM python:3.10.4-slim-buster
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN mkdir /code/
WORKDIR /code

COPY ./backend/socketserver/requirements.txt /code/requirements.txt
COPY ./backend/socketserver/main.py /code/main.py
RUN pip install -r requirements.txt

EXPOSE 514
CMD ["python3","-u","main.py"]