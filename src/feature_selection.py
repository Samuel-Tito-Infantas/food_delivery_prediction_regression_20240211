import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from sklearn.feature_selection import RFE

from sklearn.metrics import mean_squared_error


def create_plot_correlation(
    x: pd.DataFrame, y: pd.DataFrame | np.array, correlation_method: str
):
    """
    This function calculate the correlation between features and target

    Args:
        x: Features which will be using in the model training.
        y: Target for training.
        correlation_mehtod: Correlation method using for calculate the correlation.
    """
    df = x.copy()
    df["target"] = y
    corr = df.corr(method=correlation_method)
    f, ax = plt.subplots(figsize=(12, 10))
    # Generate a mask for upper traingle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # Configure a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    # Draw the heatmap
    sns.heatmap(corr, annot=True, mask=mask, cmap=cmap)


def rfe_feature_selection(
    x: pd.DataFrame,
    y: pd.DataFrame | np.array,
    model_used: str,
    num_features_to_select: int,
) -> np.array:
    """
    This function help to select the most important features for that kind of problem.

    Args:
        x: Features which will be using in the model training.
        y: Target for training.
        model_used: Model selected for run the fuction RFE.
        num_feature_to_select: Number of fetures to select.

    Returns:
        Return features selected by RFE tool
    """
    if model_used in ["LinearRegression", "RandomForestRegressor", "XGboost"]:

        model = check_model(model_used)

        # Initialize RFE with the regression model and the number of features to select
        rfe = RFE(model, n_features_to_select=num_features_to_select)

        # Fit RFE on the training data
        rfe.fit(x, y)

        # Transform the training and testing sets to include only the selected features
        X_train_selected = rfe.transform(x)

        # Fit the model on the selected features
        model.fit(X_train_selected, y)

        # Make predictions on the test set
        y_pred = model.predict(X_train_selected)

        # Evaluate the performance of the model
        mse = mean_squared_error(y, y_pred)
        print(f"Mean Squared Error: {mse}")

        # Plotting the feature ranking
        ranking_df = pd.DataFrame({"Feature": x.columns, "Ranking": rfe.ranking_})
        ranking_df = ranking_df
        plt.barh(ranking_df["Feature"], ranking_df["Ranking"])
        plt.xlabel("Ranking")
        plt.ylabel("Feature")
        plt.title("Feature Ranking with RFE")
        plt.show()

        return x.columns[rfe.support_]

    else:
        print(
            "Please, check is the parameter 'model_used' has one of each values ['LinearRegression','RandomForestRegressor','XGboost'] two of this code"
        )
        return None


def feature_importance(x: pd.DataFrame, y: pd.DataFrame | np.array, model_used: str):
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
    if model_used in ["LinearRegression", "RandomForestRegressor", "XGboost"]:
        model = check_model(model_used)
        model.fit(x, y)
        # get importance
        importance = model.feature_importances_
        # summarize feature importance
        for i, v in enumerate(importance):
            print(f"Feature: {x.columns[i]}, Score:{np.round(v,5)}")
        # plot feature importance
        plt.bar([x.columns[n] for n in range(len(importance))], importance)
        plt.xticks(rotation=30, ha="right")
        plt.show()

    else:
        print(
            "Please, check is the parameter 'model_used' has one of each values ['LinearRegression','RandomForestRegressor','XGboost'] two of this code"
        )


def check_model(
    model_used: str,
) -> LinearRegression | RandomForestRegressor | XGBRegressor | None:
    """
    Check the name of parameter 'model_used'

    Args:
        model_used: Name of the model which wanted to use.

    Returns:
        Return de ml model.
    """
    if model_used == "LinearRegression":
        return LinearRegression()

    elif model_used == "RandomForestRegressor":
        return RandomForestRegressor()

    elif model_used == "XGboost":
        return XGBRegressor()

    else:
        raise ValueError("model not founded! Please check 'model_used' value")
