FROM python:3.8-slim

RUN apt update -y && \
    apt install -y --no-install-recommends build-essential && \
    pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
