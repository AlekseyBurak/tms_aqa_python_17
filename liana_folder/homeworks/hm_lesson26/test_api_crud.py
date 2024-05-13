import requests
import json
import allure

URL = 'https://petstore.swagger.io/v2/'


@allure.id("8")
@allure.title("Create user")
def test_create_user():
    payload = {
        "id": 13,
        "username": "UsernameTest",
        "firstName": "Monica",
        "lastName": "Vasquez ",
        "email": "vasquez@mailto.plus",
        "password": "password",
        "phone": "1231231234",
        "userStatus": 0
    }

    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )

    jsn = post_response.json()
    assert post_response.status_code == 200, f"Status code {post_response.status_code} not equal 200"
    assert (jsn["code"] == 200 and
            jsn["type"] == "unknown" and
            jsn["message"] == "13"), "Response does not meet requirements"


@allure.id("2")
@allure.title("Get user by user name")
def test_get_user_by_user_name():
    payload = {
        "id": 10,
        "username": "Vasqez",
        "firstName": "Monica",
        "lastName": "Vasquez ",
        "email": "vasquez@mailto.plus",
        "password": "password",
        "phone": "1231231234",
        "userStatus": 0
    }

    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    assert post_response.status_code == 200, f"Status code {post_response.status_code} not equal 200"

    username = payload["username"]

    get_response = requests.get(
        url=f"{URL}user/{username}",
        headers={"accept": "application/json"}
    )
    jsn = get_response.json()

    assert get_response.status_code == 200, f"Status code {get_response.status_code} not equal 200"
    assert jsn == payload, "Response does not meet requirements"


@allure.id("3")
@allure.title("Updated user")
def test_update_user_by_lastname():
    payload = {
        "id": 10,
        "username": "Vasqezz",
        "firstName": "Monica",
        "lastName": "Vasquez ",
        "email": "vasquez@mailto.plus",
        "password": "password",
        "phone": "1231231234",
        "userStatus": 0
    }

    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )

    assert post_response.status_code == 200, f"Status code {post_response.status_code} not equal 200"

    username = payload["username"]

    update_payload = {
        "id": 10,
        "username": "Vasqezz",
        "firstName": "Monica",
        "lastName": "Gastambide",
        "email": "vasquez@mailto.plus",
        "password": "password",
        "phone": "1231231234",
        "userStatus": 0
    }

    put_response = requests.put(
        url=f"{URL}user/{username}",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=update_payload
    )

    jsn = update_payload
    lastname = update_payload["lastName"]

    assert put_response.status_code == 200, f"Status code {post_response.status_code} not equal 200"
    assert lastname == "Gastambide", f"lastname {post_response.status_code} not equal to New lastname"
    assert jsn == update_payload, "Response does not meet requirements"


@allure.id("4")
@allure.title("Delete user")
def test_delete_user():
    payload = {
        "id": 11,
        "username": "Vasqezz",
        "firstName": "Monica",
        "lastName": "Vasquez ",
        "email": "vasquez@mailto.plus",
        "password": "password",
        "phone": "1231231234",
        "userStatus": 0
    }

    post_response = requests.post(
        url=f"{URL}user",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )

    assert post_response.status_code == 200, f"Status code {post_response.status_code} not equal 200"

    username = payload["username"]

    delete_response = requests.delete(
        url=f"{URL}user/{username}",
        headers={"accept": "application/json"}
    )
    jsn = delete_response.json()

    assert delete_response.status_code == 200, f"Status code {delete_response.status_code} not equal 200"
    assert (jsn["code"] == 200 and
            jsn["type"] == "unknown" and
            jsn["message"] == username), "Response does not meet requirements"

    #
    # get_response = requests.get(
    #     url=f"{URL}user/{username}",
    #     headers={"accept": "application/json"}
    # )
    #
    # assert get_response.status_code == 404, f"Status code {get_response.status_code} not equal 404"


@allure.id("1")
@allure.title("Creates list of users with given input array")
def test_create_user_with_list():
    payload = [
        {
            "id": 2,
            "username": "UsernameTest",
            "firstName": "Monica",
            "lastName": "Vasquez ",
            "email": "vasquez@mailto.plus",
            "password": "password",
            "phone": "1231231234",
            "userStatus": 0
        }
    ]

    post_response = requests.post(
        url=f"{URL}user/createWithList",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )

    jsn = post_response.json()
    assert post_response.status_code == 200, f"Status code {post_response.status_code} not equal 200"
    assert (jsn["code"] == 200 and
            jsn["type"] == "unknown" and
            jsn["message"] == "ok"), "Response does not meet requirements"


@allure.id("7")
@allure.title("Creates list of users with given input array")
def test_create_user_with_array():
    payload = [
        {
            "id": 2,
            "username": "UsernameTest",
            "firstName": "Monica",
            "lastName": "Vasquez ",
            "email": "vasquez@mailto.plus",
            "password": "password",
            "phone": "1231231234",
            "userStatus": 0
        }
    ]

    post_response = requests.post(
        url=f"{URL}user/createWithArray",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )

    jsn = post_response.json()
    assert post_response.status_code == 200, f"Status code {post_response.status_code} not equal 200"
    assert (jsn["code"] == 200 and
            jsn["type"] == "unknown" and
            jsn["message"] == "ok"), "Response does not meet requirements"
