import requests
import json

URL = "https://petstore.swagger.io/v2/"

def test_get_store_inventory():
    response = requests.get(
        url=URL + "store/inventory",
        headers={"accept": "application/json"}
    )
    txt = response.text
    jsn = response.json()
    print()
    print((txt))
    print((jsn))
    assert response.status_code == 200
    assert jsn["unavailable"] == 2

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
    post_response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200
    pet_id = post_response.json()["id"]
    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    jsn = get_response.json()
    assert get_response.status_code == 200
    print()
    print(jsn)
    jsn = get_response.json()
    assert get_response.status_code == 200
    print()
    print(jsn)

def test_delete():

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
    post_response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200
    pet_id = post_response.json()["id"]

    delete_response = requests.delete(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    assert delete_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 404



