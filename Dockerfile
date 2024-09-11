FROM python:3.11-slim

WORKDIR /web_app

COPY ./requirements.txt /web_app/requirements.txt

RUN pip install --no-deps --no-cache-dir --upgrade -r /web_app/requirements.txt

COPY ./templates /web_app/templates

COPY ./main.py /web_app/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

