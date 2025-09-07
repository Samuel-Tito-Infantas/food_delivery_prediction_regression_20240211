import json
from functools import lru_cache
from app.services.ml.processor import FeaturePreprocessor


@lru_cache
def get_feature_preprocessor() -> FeaturePreprocessor:
    with open("artifacts/features_configs.json") as f:
        config = json.load(f)
    return FeaturePreprocessor(config=config)
