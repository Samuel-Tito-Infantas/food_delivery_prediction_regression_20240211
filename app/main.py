from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import food_delivery_prediction

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(
    food_delivery_prediction.router,
    prefix="/api/v1/food-delivery-prediction",
    tags=["food_delivery_prediction"],
)


@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "healthy"}
