from typing import Union
import math
import numpy as np


def vincenty_distance(
    lat1: Union[np.ndarray, float],
    lon1: Union[np.ndarray, float],
    lat2: Union[np.ndarray, float],
    lon2: Union[np.ndarray, float],
) -> np.ndarray:
    """
    This function calculate the distance between two points in base the latitude and longitude for each one of points
    using the Vicenty form.

    Args:
        lat1: Latitude of the first size .
        lon1: Longitude of the first size.
        lat2: Latitude of the second size .
        lon2: Longitude of the second size.

    Returns:
        Return de distance in KM.
    """

    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Calculate the difference between the two coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Apply the Vincenty formula
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the ellipsoid parameters
    f = 1 / 298.257223563  # flattening of the Earth's ellipsoid
    b = (1 - f) * 6371  # semi-minor axis of the Earth's ellipsoid

    return c * b  # Return the distance


def bearing_degree(
    lat1: Union[np.ndarray, float],
    lng1: Union[np.ndarray, float],
    lat2: Union[np.ndarray, float],
    lng2: Union[np.ndarray, float],
) -> np.ndarray:
    """
    This function calculate angle between two points

    Args:
        lat1: Latitude of the first size .
        lon1: Longitude of the first size.
        lat2: Latitude of the second size .
        lon2: Longitude of the second size.

    Returns:
        Return de bearing degree.
    """
    radius = 6371  # Mean radius of Earth
    diff_lng = np.radians(lng2 - lng1)
    lat1, lng1, lat2, lng2 = map(np.radians, (lat1, lng1, lat2, lng2))
    y = np.sin(diff_lng) * np.cos(lat2)
    x = np.cos(lat1) * np.sin(lat2) - np.sin(lat1) * np.cos(lat2) * np.cos(diff_lng)
    return np.degrees(np.arctan2(y, x))
