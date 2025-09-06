FROM python:3.9-slim

WORKDIR /app

COPY requirements-api.txt ./


RUN pip install --no-cache-dir -r requirements-api.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
