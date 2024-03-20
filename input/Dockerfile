FROM python:3.9-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./app /app/app

COPY ./main.py /app/main.py

COPY ./.env /app/.env

RUN mkdir /app/data

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]