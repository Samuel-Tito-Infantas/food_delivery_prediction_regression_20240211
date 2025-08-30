from functools import lru_cache
from app.core.config import settings
from app.services.predictor import DeliveryPredictorService


@lru_cache(maxsize=None)
def get_predictor_service() -> DeliveryPredictorService:
    return DeliveryPredictorService(model_path=settings.MODEL_PATH)
