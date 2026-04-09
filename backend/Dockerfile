FROM python:3.11-slim
WORKDIR /backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p model

CMD ["uvicorn", "app.app_api:app", "--host", "0.0.0.0", "--port", "8000"]