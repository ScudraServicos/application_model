
import json
import pytest
from importlib import resources

from application_model.application_model import generate_application_score


@pytest.fixture
def expected_score():
    return 0.40108762954840554


def test_generate_application_score(expected_score):
    """Test the model output score
    """
    # load payload data
    with resources.path("application_model.resources", "data.json") as path:
        print(">>> ", path)
        with open(path, "rb") as file:
            payload = file.read()

    payload_json = json.loads(payload)
    score = generate_application_score(payload_json)
    assert score == expected_score, "Score value incorrectly!"