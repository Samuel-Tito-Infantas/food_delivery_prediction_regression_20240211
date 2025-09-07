from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.core.config import settings
from app.api.v1 import food_delivery_prediction

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(
    food_delivery_prediction.router,
    prefix="/api/v1/food-delivery-prediction",
    tags=["food_delivery_prediction"],
)


@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")


@app.get("/health", tags=["Health Check"])
def health_check():
    """Verifica a saúde da aplicação."""
    return {"status": "ok", "version": settings.APP_VERSION}
