FROM python:3.14-slim

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1


RUN python -m pip install --upgrade pip setuptools wheel


COPY requirements.txt .


RUN pip install     --no-cache-dir     --retries 10     --timeout 120     -r requirements.txt


COPY . .


EXPOSE 8000


CMD ["uvicorn","api.app:app","--host","0.0.0.0","--port","8000"]
