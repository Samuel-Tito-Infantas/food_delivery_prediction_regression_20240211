from app.schemas.model_layout_v1 import InputSchema
from app.services.ml.feature_engineer import vincenty_distance, bearing_degree


class FeaturePreprocessor:
    def __init__(self, config: dict):
        self.type_of_order_mapping = config["type_of_order_mapping"]
        self.type_of_vehicle_mapping = config["type_of_vehicle_mapping"]
        self.model_features = config["model_features"]

    def transform(self, features: InputSchema) -> list:
        features_dict = features.dict()
        features_dict["Type_of_order"] = self.type_of_order_mapping.get(
            features_dict["Type_of_order"], -1
        )
        features_dict["Type_of_vehicle"] = self.type_of_vehicle_mapping.get(
            features_dict["Type_of_vehicle"], -1
        )
        features_dict["vincenty_distance"] = vincenty_distance(
            features_dict["Restaurant_latitude"],
            features_dict["Restaurant_longitude"],
            features_dict["Delivery_location_latitude"],
            features_dict["Delivery_location_longitude"],
        )

        features_dict["bearing_distance"] = bearing_degree(
            features_dict["Restaurant_latitude"],
            features_dict["Restaurant_longitude"],
            features_dict["Delivery_location_latitude"],
            features_dict["Delivery_location_longitude"],
        )

        features_scoring_list = [[features_dict[key] for key in self.model_features]]

        return features_scoring_list, features_dict
