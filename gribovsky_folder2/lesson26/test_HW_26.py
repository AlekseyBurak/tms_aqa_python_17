import requests
import json
import allure

URL = "https://petstore.swagger.io/v2/"


def test_user_create():
    payload = {
        "id": 0,
        "username": "Ivan_test",
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "email": "test_Ivan@test.com",
        "password": "Ivan11111",
        "phone": "+7 111 11 11",
        "userStatus": 0
    }
    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200


def test_user_get():
    get_response = requests.get(
        url=f"{URL}user/Ivan_test",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200
    print(get_response.json())


def test_user_update():
    payload = {
        "id": 0,
        "username": "Ivan_test_update",
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "email": "test_Ivan@test.com",
        "password": "Ivan11111",
        "phone": "+7 111 11 11",
        "userStatus": 0
    }
    update_response = requests.put(
        url=f"{URL}user/Ivan_test",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )

    assert update_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/Ivan_test_update",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200
    # jsn = get_response.json()
    # assert jsn["username"] == "Ivan_test_update"
    assert get_response.json()["username"] == "Ivan_test_update"
    print(get_response.json())


def test_correct_login_get():
    get_response = requests.get(
        url=f"{URL}user/login",
        headers={"accept": "application/json"},
        params={"username": "Ivan_test_update",
                "password": "Ivan11111"}
    )
    assert get_response.status_code == 200
    print(get_response.url)


@allure.title("incorrect work on site_side")
def test_incorrect_login_get():  # !!!! не реализовано???
    get_response = requests.get(
        url=f"{URL}user/login",
        headers={"accept": "application/json"},
        params={"username": "",
                "password": ""}
    )
    assert get_response.status_code == 400
    print(get_response.url)


def test_logout_get():
    get_response = requests.get(
        url=f"{URL}user/logout",
        headers={"accept": "application/json"},
    )
    assert get_response.status_code == 200
    print(get_response.url)


def test_delete_user():
    post_payload = {
        "id": 0,
        "username": "mishania1234",
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "email": "test_Ivan@test.com",
        "password": "Ivan11111",
        "phone": "+7 111 11 11",
        "userStatus": 0
    }
    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=post_payload
    )
    assert post_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/mishania1234",
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


def test_user_create_with_list():
    payload = [
        {
            "id": 0,
            "username": "qwerty1",
            "userStatus": 0
        },
        {
            "id": 0,
            "username": "qwerty2",
            "userStatus": 0
        },
        {
            "id": 0,
            "username": "qwerty3",
            "userStatus": 0
        }
    ]
    post_response = requests.post(
        url=f"{URL}user/createWithList",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/qwerty1",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/qwerty2",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/qwerty3",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200
    get_response = requests.get(
        url=f"{URL}user/qwerty4",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 404



