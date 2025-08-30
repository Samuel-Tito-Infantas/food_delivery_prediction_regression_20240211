from app.schemas.model_layout_v1 import InputSchema, OutputSchema
from app.services.ml.feature_engineer import vincenty_distance, bearing_degree


class FeaturePreprocessor:
    def __init__(self):
        self.type_of_order_mapping = {"Snack": 1, "Drinks": 2, "Buffet": 3, "Meal": 4}

        self.type_of_vehicle_mapping = {
            "motorcycle": 1,
            "scooter": 2,
            "electric_scooter": 3,
            "bicycle": 4,
        }

        self.scoring_features = [
            "Delivery_person_Age",
            "Delivery_person_Ratings",
            "Type_of_vehicle",
            "vincenty_distance",
            "bearing_distance",
        ]

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

        features_scoring_list = [[features_dict[key] for key in self.scoring_features]]

        return features_scoring_list, features_dict
