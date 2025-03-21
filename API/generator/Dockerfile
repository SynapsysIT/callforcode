FROM python:3.12-bullseye

COPY app/ /app

WORKDIR /app
RUN apt-get update -y && apt-get upgrade -y
RUN cd /app && pip install -r requirements.txt



CMD ["uvicorn", "main:app", "--host",  "0.0.0.0", "--port", "8000"]
