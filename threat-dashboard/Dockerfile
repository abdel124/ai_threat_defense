FROM python:3.11-slim

WORKDIR /app
COPY ./app /app/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "app/main.py", \
     "--server.enableXsrfProtection=false", \
     "--server.enableCORS=false", \
     "--server.fileWatcherType=none", \
     "--server.port=8501", \
     "--server.address=0.0.0.0"]