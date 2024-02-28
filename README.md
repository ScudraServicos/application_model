# application_model

Generate application score for new customers.

- [Documentation](https://scudraservicos.github.io/application_model/)

## Installation

[PyPI Package](https://pypi.org/project/application_model/)

```bash
$ pip install application_model
```

## Usage

`application_model` can be used to generate application score as follows:

```python
from application_model.application_model import generate_application_score

payload = {
   "ume-profession":"COSTUREIRA",
   "ume-zipcode":69059192.0,
   "ume-age_on_application":63.0,
   "ume-segment":"Móveis",
   "ume-retailer":"apa-moveis",
   "ume-city":"MANAUS",
   "ume-state":"AMAZONAS",
   "bvsIncome-CLASSRENDAV2":6.0,
   "bvsIncome-RendaPresumida":1700.0,
   "bvsP5-Score":0.3009,
   "bvsSubP5-Fintechs":0.4499,
   "bvsSubP5-CartaoCredito":0.3950,
   "bvsSubP5-CreditoPessoal":0.4589,
   "bvsSubP5-VAR_MoveisEletrodomesticos":0.3379,
   "bvsSubP5-VAR_VestuarioAcessorios":0.2430,
   "bvsSubP5-FinancialmentoVeiculos":0.4199
}

payload_json = json.loads(payload)
score = generate_application_score(payload_json)
```


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`application_model` was created by Wesllen Sousa Lima. It is licensed under the terms of the Proprietary license.

## Credits

`application_model` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
