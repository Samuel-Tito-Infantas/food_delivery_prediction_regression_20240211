import pickle

feature_used = [
    "Delivery_person_Age",
    "Delivery_person_Ratings",
    "Type_of_vehicle",
    "vincenty_distance",
    "bearing_distance",
]

# Type_of_order

dic_values_name = {
    "Snack ": 1,
    "Drinks ": 2,
    "Buffet ": 3,
    "Meal ": 4,
    # Type_of_vehicle
    "motorcycle ": 1,
    "scooter ": 2,
    "electric_scooter ": 3,
    "bicycle ": 4,
}


def load_model_pickle(filename: str):
    """Load a model from disk using pickle."""
    with open(filename, "rb") as f:
        model = pickle.load(f)
    print(f"Model loaded from {filename}")
    return model
