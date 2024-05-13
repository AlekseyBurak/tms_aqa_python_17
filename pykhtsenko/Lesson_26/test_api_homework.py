import requests
import json

URL = "https://petstore.swagger.io/v2/"

def test_create_user():
    payload = {
        "id": 0,
        "username": "Agny",
        "firstName": "Yana",
        "lastName": "Yana",
        "email": "string",
        "password": "12345",
        "phone": "string",
        "userStatus": 0
    }

    # Создание нового пользователя
    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200


# тест на удаление данных юзера
def test_delete_user():
    payload = {
        "id": 0,
        "username": "Agny",
        "firstName": "Yana",
        "lastName": "Yana",
        "email": "string",
        "password": "12345",
        "phone": "string",
        "userStatus": 0
    }

    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200
    user_name = post_response.json()["username"]

    delete_response = requests.delete(
        url=f"{URL}user/{user_name}",
        headers={"accept": "application/json"}
    )
    assert delete_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/{user_name}",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 404

# тест на обновление данных для юзера
def test_update_user():
    payload = {
        "id": 0,
        "username": "Agny",
        "firstName": "Yana",
        "lastName": "Yana",
        "email": "string",
        "password": "12345",
        "phone": "string",
        "userStatus": 0
    }
    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200
    user_name = post_response.json()["username"]

    update_payload = {
        "id": 0,
        "username": "Pop",
        "firstName": "Test",
        "lastName": "Test",
        "email": "string",
        "password": "1234588",
        "phone": "string",
        "userStatus": 0
    }

    put_response = requests.put(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=update_payload
    )
    assert put_response.status_code == 200

