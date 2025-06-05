FROM python:3.11-slim

# Install Streamlit and other dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
 && pip uninstall -y watchdog  # This removes inotify watcher

# Copy source code
COPY . /app
WORKDIR /app

# Entrypoint: run Streamlit without file watching
CMD ["streamlit", "run", "app/main.py", \
     "--server.enableXsrfProtection=false", \
     "--server.fileWatcherType=none", \
     "--server.port=8501", \
     "--server.address=0.0.0.0"]
