import requests
from URLs import GET_USER_URL, CREATE_LIST_OF_USERS_URL, CREATE_LIST_OF_USERS_WITH_ARRAY_URL, CREATE_USER_URL, \
    DELETE_USER_URL
from mock_data import FIRST_USER_PAYLOAD, SECOND_USER_PAYLOAD
import allure


class TestUserPostRequests:
    @allure.feature("POST")
    @allure.title("Create list of users")
    @allure.id("1")
    def test_create_list_of_users(self):
        try:
            payload = [FIRST_USER_PAYLOAD, SECOND_USER_PAYLOAD]
            response = requests.post(
                url=CREATE_LIST_OF_USERS_URL,
                headers={"accept": "application/json", "Content-Type": "application/json"},
                json=payload
            )

            jsn = response.json()

            assert response.status_code == 200
            assert jsn["message"] == 'ok'

            response = requests.get(
                url=f'{GET_USER_URL}/{FIRST_USER_PAYLOAD["username"]}',
                headers={"accept": "application/json"}
            )

            jsn1 = response.json()
            del jsn1["id"]

            assert response.status_code == 200
            assert jsn1 == FIRST_USER_PAYLOAD

            response = requests.get(
                url=f'{GET_USER_URL}/{SECOND_USER_PAYLOAD["username"]}',
                headers={"accept": "application/json"}
            )

            jsn2 = response.json()
            del jsn2["id"]

            assert response.status_code == 200
            assert jsn2 == SECOND_USER_PAYLOAD

        finally:
            requests.delete(
                url=f'{DELETE_USER_URL}/{FIRST_USER_PAYLOAD["username"]}'
            )

            requests.delete(
                url=f'{DELETE_USER_URL}/{SECOND_USER_PAYLOAD["username"]}'
            )

    @allure.feature("POST")
    @allure.title("Create list of users with array")
    @allure.id("1")
    def test_create_list_of_users_with_array(self):
        try:
            payload = [FIRST_USER_PAYLOAD, SECOND_USER_PAYLOAD]
            response = requests.post(
                url=CREATE_LIST_OF_USERS_WITH_ARRAY_URL,
                headers={"accept": "application/json", "Content-Type": "application/json"},
                json=payload
            )

            jsn = response.json()

            assert response.status_code == 200
            assert jsn["message"] == 'ok'

            response = requests.get(
                url=f'{GET_USER_URL}/{FIRST_USER_PAYLOAD["username"]}',
                headers={"accept": "application/json"}
            )

            jsn1 = response.json()
            del jsn1["id"]

            assert response.status_code == 200
            assert jsn1 == FIRST_USER_PAYLOAD

            response = requests.get(
                url=f'{GET_USER_URL}/{SECOND_USER_PAYLOAD["username"]}',
                headers={"accept": "application/json"}
            )

            jsn2 = response.json()
            del jsn2["id"]

            assert response.status_code == 200
            assert jsn2 == SECOND_USER_PAYLOAD

        finally:
            requests.delete(
                url=f'{DELETE_USER_URL}/{FIRST_USER_PAYLOAD["username"]}'
            )

            requests.delete(
                url=f'{DELETE_USER_URL}/{SECOND_USER_PAYLOAD["username"]}'
            )

    @allure.feature("POST")
    @allure.title("Create user")
    @allure.id("1")
    def test_create_user(self):
        try:
            payload = FIRST_USER_PAYLOAD
            response = requests.post(
                url=CREATE_USER_URL,
                headers={"accept": "application/json", "Content-Type": "application/json"},
                json=payload
            )

            jsn = response.json()

            assert response.status_code == 200
            assert jsn["code"] == 200

            response = requests.get(
                url=f'{GET_USER_URL}/{FIRST_USER_PAYLOAD["username"]}',
                headers={"accept": "application/json"}
            )

            jsn1 = response.json()
            del jsn1["id"]

            assert response.status_code == 200
            assert jsn1 == FIRST_USER_PAYLOAD

        finally:
            requests.delete(
                url=f'{DELETE_USER_URL}/{FIRST_USER_PAYLOAD["username"]}'
            )
