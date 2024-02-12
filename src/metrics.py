import pandas as pd
import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_squared_log_error,
    median_absolute_error,
    r2_score,
    explained_variance_score,
)


def metrics_values(
    y_true: pd.DataFrame | np.array, y_pred: pd.DataFrame | np.array
) -> pd.DataFrame:
    """
    This function calculate differente metrics for regression problems

    Args:
        y_true: The teste target.
        y_pred: The predicted target.

    Returns:
        Return DataFrame with the all of the regretion metrics.
    """
    mae = mean_absolute_error(y_true, y_pred)  # Mean Absolute Error (MAE)
    print(f"Mean Absolute Error (MAE): {mae}")

    mse = mean_squared_error(y_true, y_pred)  # Mean Squared Error (MSE)
    print(f"Mean Squared Error (MSE): {mse}")

    rmse = mean_squared_error(
        y_true, y_pred, squared=False
    )  # Root Mean Squared Error (RMSE)
    print(f"Root Mean Squared Error (RMSE): {rmse}")

    msle = mean_squared_log_error(
        y_true, y_pred
    )  # Mean Squared Logarithmic Error (MSLE)
    print(f"Mean Squared Logarithmic Error (MSLE): {msle}")

    medae = median_absolute_error(y_true, y_pred)  # Median Absolute Error
    print(f"Median Absolute Error (MedAE): {medae}")

    r2 = r2_score(y_true, y_pred)  # R-squared (R2)
    print(f"R-squared (R2): {r2}")

    explained_var = explained_variance_score(y_true, y_pred)  # Explained Variance Score
    print(f"Explained Variance Score: {explained_var}")

    return pd.DataFrame(
        {
            "Mean Absolute Error (MAE)": [mae],
            "Mean Squared Error (MSE)": [mse],
            "Root Mean Squared Error (RMSE)": [rmse],
            "Mean Squared Logarithmic Error (MSLE)": [msle],
            "Median Absolute Error (MedAE)": [medae],
            "R-squared (R2)": [r2],
            "Explained Variance Score": [explained_var],
        }
    )
