
import json
import pytest
from importlib import resources

from application_model.application_model import generate_application_score


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
    return [
        'ume-profession', 'ume-zipcode', 'ume-age_on_application', 'ume-segment', 
        'ume-retailer', 'ume-city', 'ume-state', 'bvsIncome-CLASSRENDAV2', 'bvsIncome-RendaPresumida', 
        'bvsP5-Score', 'bvsSubP5-Fintechs', 'bvsSubP5-CartaoCredito', 'bvsSubP5-CreditoPessoal', 
        'bvsSubP5-VAR_MoveisEletrodomesticos', 'bvsSubP5-VAR_VestuarioAcessorios', 'bvsSubP5-FinancialmentoVeiculos'
    ]

@pytest.fixture
def expected_score():
    return 0.40108762954840554


def test_payload_structure(payload, expected_keys):
    """Test the payload structure
    """
    keys = list(payload.keys())

    assert len(keys) == len(expected_keys), "Number of columns of the payload are incorrect!"
    assert keys == expected_keys, "Columns name of the payload are incorrect!"

def test_generate_application_score(payload, expected_score):
    """Test the model output score
    """
    score = generate_application_score(payload)
    assert score == expected_score, "Incorrect score value!"
