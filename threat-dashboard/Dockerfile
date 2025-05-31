FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables directly to avoid issues with Streamlit watchers
ENV STREAMLIT_SERVER_FILEWATCHERTYPE=none \
    STREAMLIT_SERVER_ENABLECORS=false \
    STREAMLIT_SERVER_ENABLEXSRFPROTECTION=false

CMD ["streamlit", "run", "dashboard.py"]