from fastapi import APIRouter, Depends
from app.schemas.model_layout_v1 import InputSchema, OutputSchema
from app.services.predictor import DeliveryPredictorService
from app.dependencies.predictor import get_predictor_service

router = APIRouter()


@router.post("/predict", response_model=OutputSchema)
def predict(
    input_data: InputSchema,
    predictor_service: DeliveryPredictorService = Depends(get_predictor_service),
):
    result = predictor_service.predict(input_data)
    return OutputSchema(predict_result=result)
