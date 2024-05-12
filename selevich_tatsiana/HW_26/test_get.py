import requests
from URLs import GET_USER_URL, LOGIN_URL, LOGOUT_URL
import allure


class TestUserGetRequests:
    @allure.feature("GET")
    @allure.title("Get user by username")
    @allure.id("1")
    @allure.severity("Major")
    @allure.story("JQ-1")
    def test_get_user_by_username(self, create_user):
        response = requests.get(
            url=f'{GET_USER_URL}/{create_user["username"]}',
            headers={"accept": "application/json"}
        )

        jsn = response.json()
        del jsn["id"]

        assert response.status_code == 200
        assert jsn == create_user

    @allure.feature("GET")
    @allure.title("Login user")
    @allure.id("1")
    def test_login(self):
        query_params = {"username": "Tanya", "password": "123"}
        response = requests.get(
            url=LOGIN_URL,
            params=query_params,
            headers={"accept": "application/json"}
        )

        jsn = response.json()

        assert response.status_code == 200
        assert jsn["code"] == 200

    @allure.feature("GET")
    @allure.title("Logout user")
    @allure.id("1")
    def test_logout(self):
        response = requests.get(
            url=LOGOUT_URL,
            headers={"accept": "application/json"}
        )

        jsn = response.json()

        assert response.status_code == 200
        assert jsn["message"] == 'ok'
