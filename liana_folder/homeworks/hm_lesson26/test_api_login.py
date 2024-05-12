import requests
import json
import allure

URL = 'https://petstore.swagger.io/v2/'


@allure.id("5")
@allure.title("Logs user into the system")
def test_login():
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
    password = payload["password"]

    get_response = requests.get(
        url=f"{URL}user/login?username={username}&password={password}",
        headers={"accept": "application/json"}
    )
    jsn = get_response.json()

    assert get_response.status_code == 200, f"Status code {get_response.status_code} not equal 200"
    assert (jsn["code"] == 200 and
            jsn["type"] == "unknown"), "Response does not meet requirements"


@allure.id("6")
@allure.title("Logs out current logged in user session")
def test_logout():
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
    password = payload["password"]

    get_response_login = requests.get(
        url=f"{URL}user/login?username={username}&password={password}",
        headers={"accept": "application/json"}
    )
    jsn = get_response_login.json()

    assert get_response_login.status_code == 200, f"Status code {get_response_login.status_code} not equal 200"

    get_response_logout = requests.get(
        url=f"{URL}user/logout",
        headers={"accept": "application/json"}
    )
    jsn_logout = get_response_logout.json()

    assert get_response_logout.status_code == 200, f"Status code {get_response_logout.status_code} not equal 200"
    assert (jsn_logout["code"] == 200 and
            jsn_logout["type"] == "unknown" and
            jsn_logout["message"] == "ok"), "Response does not meet requirements"
