FROM python:3.12-slim

ARG APP_NAME_DEFAULT="App-default-values"
ARG APP_VERSION_DEFAULT="0.0.0"
ARG MODEL_PATH_DEFAULT="/app/default_model.pkl"

ENV APP_NAME=${APP_NAME_DEFAULT}
ENV APP_VERSION=${APP_VERSION_DEFAULT}
ENV MODEL_PATH=${MODEL_PATH_DEFAULT}


WORKDIR /app

COPY requirements-api.txt ./

RUN pip install --no-cache-dir -r requirements-api.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
