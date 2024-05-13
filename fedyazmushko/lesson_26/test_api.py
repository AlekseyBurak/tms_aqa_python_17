import json

import requests


URL = "https://petstore.swagger.io/v2/"

def test_get_store_inventory():
    response = requests.get(
        url=f"{URL}store/inventory",
        headers={"accept": "application/json"}
    )
    jsn = response.json()
    assert jsn["unavailable"] == 2
    assert response.status_code == 200

def test_add_pet():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "Amily",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        # data=json.dumps(payload),
        json=payload
    )
    assert response.status_code == 200
    print()
    print(response.json())