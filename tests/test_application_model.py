
import pytest
from application_model.application_model import generate_application_score


@pytest.fixture
def expected_score():
    return 0.8973


def test_generate_application_score(expected_score):
    """Test the model output score
    """
    score = generate_application_score({})
    assert score == expected_score, "Score value incorrectly!"