# Use official Python base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Disable watchdog observer for containerized environments
# Disable XSRF protection for cross-origin requests
CMD ["streamlit", "run", "threat-dashboard/app/main.py", \
     "--server.enableXsrfProtection=false", \
     "--server.runOnSave=false", \
     "--server.enableCORS=false", \
     "--server.enableStaticServing=false", \
     "--server.fileWatcherType=none", \
     "--server.port=8501", \
     "--server.address=0.0.0.0"]
