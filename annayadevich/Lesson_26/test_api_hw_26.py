import requests
import json

URL = "https://petstore.swagger.io/v2/"


def test_create_user():  # POST/user Create user
    payload = {
        "id": 1,
        "username": "anna_new",
        "firstName": "Anna",
        "lastName": "Novik",
        "email": "annanew@mailinator.com",
        "password": "Password1",
        "phone": "+375 44 33",
        "userStatus": 0
    }
    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200


def test_get_user():  # GET/user/{username} Get user by user name
    get_response = requests.get(
        url=f"{URL}user/anna_new",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200
    print(get_response.json())


def test_user_login():  # GET/user/login Logs user into the system
    get_response = requests.get(
        url=f"{URL}user/login",
        headers={"accept": "application/json"},
        params={"username": "anna_new",
                "password": "Password1"}
    )
    assert get_response.status_code == 200
    print(get_response.url)


def test_user_logout():  # GET/user/logout Logs out current logged in user session
    get_response = requests.get(
        url=f"{URL}user/logout",
        headers={"accept": "application/json"},
    )
    assert get_response.status_code == 200
    print(get_response.url)


def test_create_user_with_list():  # POST/user/createWithList Creates list of users with given input array
    payload = [
        {
            "id": 2,
            "username": "user_1",
            "firstName": "Ron",
            "lastName": "Weasley ",
            "email": "ronnew@mailinator.com",
            "password": "Password123",
            "phone": "+375 44 33",
            "userStatus": 1
        },
        {
            "id": 3,
            "username": "user_2",
            "firstName": "Harry",
            "lastName": "Potter",
            "email": "potter@mailinator.com",
            "password": "123Passowrd",
            "phone": "+375 44 11",
            "userStatus": 1
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
        url=f"{URL}user/user_1",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/user_2",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/user_3",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 404


def test_update_user():  # PUT/user/{username} Updated user
    payload = {
        "id": 4,
        "username": "user_3",
        "firstName": "Hermione",
        "lastName": "Granger",
        "email": "hermione@mailinator.com",
        "password": "123Passowrd123",
        "phone": "+375 44 13",
        "userStatus": 1
    }
    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200

    update_payload = {
        "id": 4,
        "username": "user_3",
        "firstName": "Hermione123",
        "lastName": "Granger",
        "email": "hermione@mailinator.com",
        "password": "123Passowrd123",
        "phone": "+375 44 13",
        "userStatus": 1
    }
    put_response = requests.put(
        url=f"{URL}user/user_3",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=update_payload
    )
    assert put_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/user_3",
        headers={"accept": "application/json"}
    )
    assert get_response.status_code == 200
    assert get_response.json()["firstName"] == "Hermione123"


def test_delete_user(): #DELETE/user/{username} Delete user
    post_payload = {
        "id": 5,
        "username": "user_5",
        "firstName": "Lord",
        "lastName": "Voldemort",
        "email": "lorde@mailinator.com",
        "password": "123Passowrd123",
        "phone": "+375 44 13",
        "userStatus": 1
    }
    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=post_payload
    )
    assert post_response.status_code == 200

    get_response = requests.get(
        url=f"{URL}user/user_5",
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