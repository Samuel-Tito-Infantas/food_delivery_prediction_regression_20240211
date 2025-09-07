import os
import sys

import pytest
import operator
import json

project_root = os.getcwd()

if project_root not in sys.path:
    sys.path.insert(0, project_root)


print("*"*80)
print(os.getcwd())
from app.schemas.model_layout_v1 import InputSchema
from app.services.ml.processor import FeaturePreprocessor
#from artifacts import features_configs
# 2. Open and load the data from the JSON file.



def test_feature_preprocessor_transform():
    sample_input = InputSchema(
        ID="4607",
        Delivery_person_ID = "INDORES13DEL02",
        Delivery_person_Age =  37,
        Delivery_person_Ratings = 4.9,
        Restaurant_latitude = 22.745049,
        Restaurant_longitude = 75.892471,
        Delivery_location_latitude = 22.765049,
        Delivery_location_longitude = 75.912471,
        Type_of_order =  "Snack",
        Type_of_vehicle = "motorcycle",
        Time_taken = 24
    )

    config_file_path = os.path.join("artifacts", "features_configs.json")

    with open(config_file_path, 'r') as f:
        dict_features_configs = json.load(f)

    preprocessor = FeaturePreprocessor(config=dict_features_configs)
    features_list, features_dict = preprocessor.transform(sample_input)
    expected_features_list = [[37, 4.9, 1, 3.015006532890031, 42.67735687418738]]
    assert features_list == expected_features_list