import requests
import json


URL = 'https://petstore.swagger.io/v2/'


def test_get_store_inventory():
    response = requests.get(
        url=f"{URL}store/inventory",
        headers={"accept": "application/json"}
    )
    print()
    print(response)
    assert response.status_code == 200
    # assert jsn["unavailable"] == 3

def test_create_pet():
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


def test_delete_pet():
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


def test_update_pet():
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

    update_payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "dog"
        },
        "name": "Amily1",
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

    put_response = requests.post(
        url=f"{URL}pet",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=update_payload
    )
    assert put_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}pet/{pet_id}",
        headers={"accept": "application/json"}
    )
    jsn = get_response.json()
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Amily1"
