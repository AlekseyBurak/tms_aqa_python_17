import requests
import json

URL = "https://petstore.swagger.io/v2/"


def test_add_check_user():
    payload = {
        "id": 0,
        "username": "Palina",
        "firstName": "Palina",
        "lastName": "Novik",
        "email": "string",
        "password": "string",
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
    print(json)
    # username = post_response.json()["username"]
    get_response = requests.get(
        url=f"{URL}user/Palina",
        headers={"accept": "application/json"}
    )
    jsn = get_response.json()
    assert get_response.status_code == 200
    assert get_response.json()["username"] == "Palina"
    assert get_response.json()["firstName"] == "Palina"
    assert get_response.json()["lastName"] == "Novik"
    print()
    print(jsn)


def test_update_check_user():
    payload = {
        "id": 0,
        "username": "Palina",
        "firstName": "Novik",
        "lastName": "Novik",
        "email": "string",
        "password": "string",
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

    payload_2 = {
        "id": 0,
        "username": "Palina_user",
        "firstName": "Palina",
        "lastName": "Novik23",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    put_response = requests.put(
        url=f"{URL}user/Palina",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload_2
    )
    assert put_response.status_code == 200
    print(json)
    # username = post_response.json()["username"]
    get_response = requests.get(
        url=f"{URL}user/Palina_user",
        headers={"accept": "application/json"}
    )
    jsn = get_response.json()
    assert get_response.status_code == 200
    assert get_response.json()["username"] == "Palina_user"
    assert get_response.json()["firstName"] == "Palina"
    assert get_response.json()["lastName"] == "Novik23"
    print()
    print(jsn)


def test_delete_check_user():
    payload = {
        "id": 0,
        "username": "Palina",
        "firstName": "Novik",
        "lastName": "Novik",
        "email": "string",
        "password": "string",
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

    delete_response = requests.delete(
        url=f"{URL}user/Palina",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert delete_response.status_code == 200
    # username = post_response.json()["username"]
    get_response = requests.get(
        url=f"{URL}user/Palina",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200


def test_create_login_logout_user():
    payload = {
        "id": 0,
        "username": "Palina",
        "firstName": "Palina",
        "lastName": "Badgley",
        "email": "string",
        "password": "Badgley",
        "phone": "string",
        "userStatus": 0
    }
    post_response_new = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response_new.status_code == 200
    username = post_response_new.json()["username"]
    get_response = requests.get(
        url=f"{URL}user/{username}",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200

    username = post_response_new.json()["username"]
    password_id = post_response_new.json()["password"]

    get_response_login = requests.get(
        url=f"{URL}user/login{username}{password_id}",
        headers={"accept": "application/json"}
    )
    assert get_response_login.status_code == 200


    get_response_logout = requests.get(
        url=f"{URL}user/logout",
        headers={"accept": "application/json"}
    )
    assert get_response_logout.status_code == 200
