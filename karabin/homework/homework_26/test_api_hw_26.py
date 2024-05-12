import requests
import allure
import json

URL = "https://petstore.swagger.io/v2/"


def test_user_name():
    payload = {
        "id": 0,
        "username": "Al_123",
        "firstName": "Alex",
        "lastName": "Kara",
        "email": "sdf@mail.ru",
        "password": "qwer123",
        "phone": "+375255555555",
        "userStatus": 0
    }
    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200


@allure.testcase(url=URL)
def test_get_user_name():
    get_response = requests.get(
        url=f"{URL}user/Al_123",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200


def test_put_user_name():
    payload = {
        "id": 0,
        "username": "Al_123_Al",
        "firstName": "Alex",
        "lastName": "Kara",
        "email": "sdf@mail.ru",
        "password": "qwer123",
        "phone": "+375255555555",
        "userStatus": 0
    }
    put_response = requests.put(
        url=f"{URL}user/Al_123_Al",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert put_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/Al_123_Al",
        headers={"accept": "application/json"}
    )
    assert get_response.json()["username"] != "Al_123_+"

    get_response = requests.get(
        url=f"{URL}user/Al_123_p",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 404


def test_delete_user_name():
    payload = {
        "id": 0,
        "username": "alex",
        "firstName": "Alex",
        "lastName": "Kara",
        "email": "sdf@mail.ru",
        "password": "qwer123",
        "phone": "+375255555555",
        "userStatus": 0
    }
    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/alex",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200
    user_name = get_response.json()["username"]

    del_response = requests.delete(
        url=f"{URL}user/{user_name}",
        headers={"accept": "application/json"},
    )
    assert del_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/{user_name}",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 404


def test_login_user():
    payload = {
        "username": "alex",
        "password": "qwer123",
    }
    get_response = requests.get(
        url=f"{URL}user/login",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload

    )
    assert get_response.status_code == 200


def test_logout_user():
    payload = {
        "username": "alex",
        "password": "qwer123",
    }
    get_response_logout = requests.get(
        url=f"{URL}user/logout",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload

    )
    assert get_response_logout.status_code == 200


def test_create_user():
    payload = [
        {
            "id": 0,
            "username": "Al_123",
            "firstName": "Alex",
            "lastName": "Kara",
            "email": "sdf@mail.ru",
            "password": "qwer123",
            "phone": "+375255555555",
            "userStatus": 0
        }
    ]

    post_response = requests.post(
        url=f"{URL}user/createWithArray",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200



def test_create():
    payload = {
        "id": 1,
        "username": "Al_123",
        "firstName": "Alex",
        "lastName": "Kara",
        "email": "sdf@mail.ru",
        "password": "qwer123",
        "phone": "+375255555555",
        "userStatus": 0
    }
    get_response = requests.get(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload

    )
    assert get_response.status_code == 405

