import pickle
from app.schemas.model_layout_v1 import InputSchema, OutputSchema
from app.services.ml.processor import FeaturePreprocessor


class DeliveryPredictorService:
    def __init__(self, model_path: str):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, input_data: InputSchema) -> OutputSchema:
        preprocessor = FeaturePreprocessor()
        preprocessed_scoring_list, preprocessed_data = preprocessor.transform(
            input_data
        )

        print("preprocessed_scoring_list:", preprocessed_scoring_list)
        print("preprocessed_data:", preprocessed_data)

        prediction = self.model.predict(preprocessed_scoring_list)
        print("prediction 1 :", prediction)
        prediction = prediction[0]

        return float(prediction)
