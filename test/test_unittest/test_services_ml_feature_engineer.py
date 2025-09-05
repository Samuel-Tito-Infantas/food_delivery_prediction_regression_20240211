import os
import sys

import pytest
import operator

project_root = os.getcwd()

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from app.services.ml.feature_engineer import vincenty_distance, bearing_degree


@pytest.mark.parametrize("lat1, lon1, lat2, lon2, expected_distance, comparison_op", [
    pytest.param(51.5074, 0.1278, 48.8566, 2.3522, 333.4543675369089, operator.eq, id="True_case"),
    pytest.param(51.321, 0.321321278, 8.8566, 2.3522, 333.4543675369089, operator.ne, id="False_case"),
])

def test_calculate_vincenty_distance(lat1, lon1, lat2, lon2, expected_distance, comparison_op):
    result = vincenty_distance(lat1, lon1, lat2, lon2)
    assert comparison_op(result, expected_distance)

@pytest.mark.parametrize("lat1, lon1, lat2, lon2, expected_distance, comparison_op", [
    pytest.param(51.5074, 0.1278, 48.8566, 2.3522, 150.88914995232093, operator.eq, id="True_case_1"),
    pytest.param(1.5074, 0.1278, 8.8566, 2.3522, 150.88914995232093, operator.ne, id="False_case_1"),
])
def test_calculate_bearing_degree(lat1, lon1, lat2, lon2, expected_distance, comparison_op):
    result = bearing_degree(lat1, lon1, lat2, lon2)
    assert comparison_op(result, expected_distance)