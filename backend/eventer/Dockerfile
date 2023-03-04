FROM python:3.11.2-alpine
RUN mkdir /code
WORKDIR /code
COPY ./backend/eventer/requirements.txt /code
RUN pip install -r requirements.txt
COPY ./backend/eventer/cleandata.py /code
ENV PYTHONUNBUFFERED 1
CMD ["python3","cleandata.py"]