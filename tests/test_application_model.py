
import json
import pytest
from importlib import resources

from application_model.application_model import generate_application_score
from application_model.utils.constants import PAYLOAD_SCHEMA


@pytest.fixture
def payload():
    # load payload data
    with resources.path("application_model.resources", "data.json") as path:
        print(">>> ", path)
        with open(path, "rb") as file:
            payload = file.read()
    return json.loads(payload)

@pytest.fixture
def expected_keys():
    return PAYLOAD_SCHEMA

@pytest.fixture
def expected_score():
    return 0.41316487120280165


def test_payload_structure(payload, expected_keys):
    """Test the payload structure
    """
    keys = list(payload.keys())

    assert len(keys) == len(expected_keys), "Number of payload columns are incorrect!"
    assert keys == expected_keys, "Payload columns names are incorrect!"

def test_generate_application_score(payload, expected_score):
    """Test the model output score
    """
    score = generate_application_score(payload)
    assert score == expected_score, "Incorrect score value!"
