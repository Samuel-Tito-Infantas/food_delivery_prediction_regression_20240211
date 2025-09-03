import pickle
from app.schemas.model_layout_v1 import InputSchema, OutputSchema
from app.services.ml.processor import FeaturePreprocessor


class DeliveryPredictorService:
    def __init__(self, model_path: str, preprocessor: FeaturePreprocessor) :
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        self.preprocessor = preprocessor


    def predict(self, input_data: InputSchema) -> float:
        preprocessed_scoring_list, preprocessed_data = self.preprocessor.transform(
            input_data
        )

        print("preprocessed_scoring_list:", preprocessed_scoring_list)
        print("preprocessed_data:", preprocessed_data)

        prediction = self.model.predict(preprocessed_scoring_list)
        print("prediction 1 :", prediction)
        prediction = prediction[0]

        return float(prediction)
