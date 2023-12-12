FROM python:3.11-slim
COPY app /app
WORKDIR /app
RUN apt-get update && \
    apt-get upgrade -y
RUN apt-get install libreoffice -y
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]