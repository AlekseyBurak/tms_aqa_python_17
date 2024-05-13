import requests
from mock_data import FIRST_USER_PAYLOAD, SECOND_USER_PAYLOAD
from URLs import GET_USER_URL, UPDATE_USER_URL, DELETE_USER_URL
import allure


class TestUserPutRequests:
    @allure.feature("PUT")
    @allure.title("Update user")
    @allure.id("1")
    def test_update_user(self, create_user):
        try:
            response = requests.put(
                url=f'{UPDATE_USER_URL}/{FIRST_USER_PAYLOAD["username"]}',
                headers={"accept": "application/json", "Content-Type": "application/json"},
                json=SECOND_USER_PAYLOAD
            )

            jsn = response.json()

            assert response.status_code == 200
            assert jsn["code"] == 200

            response = requests.get(
                url=f'{GET_USER_URL}/{SECOND_USER_PAYLOAD["username"]}',
                headers={"accept": "application/json"}
            )

            jsn1 = response.json()
            del jsn1["id"]

            assert response.status_code == 200
            assert jsn1 == SECOND_USER_PAYLOAD

        finally:
            requests.delete(
                url=f'{DELETE_USER_URL}/{SECOND_USER_PAYLOAD["username"]}'
            )
