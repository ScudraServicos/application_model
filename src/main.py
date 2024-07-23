
import json
from importlib import resources

from application_model.application_model import generate_application_score

# load payload data
with resources.path("application_model.resources", "data.json") as path:
    print(">>> ", path)
    with open(path, "rb") as file:
        payload = file.read()

# transform payload in python dict
payload_json = json.loads(payload)

# generate score
score = generate_application_score(payload_json)
print(">>>", score)
