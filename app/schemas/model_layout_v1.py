from pydantic import BaseModel, Field


class InputSchema(BaseModel):
    ID: str = Field(..., description="ID of the delivery", example="4607")
    Delivery_person_ID: str = Field(
        ..., description="ID of deliver person", example="INDORES13DEL02"
    )
    Delivery_person_Age: int = Field(
        ..., description="Age of deliver person", example=37
    )
    Delivery_person_Ratings: float = Field(
        ..., description="Ratings of deliver person", example=4.9
    )
    Restaurant_latitude: float = Field(
        ..., description="Latitude of restaurant", example=12.9716
    )
    Restaurant_longitude: float = Field(
        ..., description="Longitude of restaurant", example=77.5946
    )
    Delivery_location_latitude: float = Field(
        ..., description="Latitude of delivery location", example=12.2958
    )
    Delivery_location_longitude: float = Field(
        ..., description="Longitude of delivery location", example=76.6394
    )
    Type_of_order: str = Field(..., description="Type of order", example="Snack")
    Type_of_vehicle: str = Field(
        ..., description="Type of vehicle", example="motorcycle"
    )
    Time_taken: int = Field(..., description="Time taken for delivery", example=30)


class OutputSchema(BaseModel):
    predict_result: float = Field(
        ...,
        description="Predicted time taken for delivery in minutes",
        example=24.951336,
    )
