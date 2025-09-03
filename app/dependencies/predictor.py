from fastapi import Depends
from functools import lru_cache

from app.core.config import settings
from app.services.predictor import DeliveryPredictorService
from app.dependencies.preprocessor import get_feature_preprocessor
from app.services.ml.processor import FeaturePreprocessor


@lru_cache(maxsize=None)
def get_predictor_service(preprocessor: FeaturePreprocessor = Depends(get_feature_preprocessor)) -> DeliveryPredictorService:
    service = DeliveryPredictorService(model_path=settings.MODEL_PATH, preprocessor=preprocessor)
    return service
