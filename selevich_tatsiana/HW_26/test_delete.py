import requests
from URLs import GET_USER_URL, DELETE_USER_URL
import allure


class TestUserDeleteRequests:
    @allure.feature("DELETE")
    @allure.title("Delete user")
    @allure.id("1")
    def test_delete_user(self, create_user):
        response = requests.delete(
            url=f'{DELETE_USER_URL}/{create_user["username"]}',
            headers={"accept": "application/json"}
        )

        jsn = response.json()

        assert response.status_code == 200
        assert jsn["message"] == create_user["username"]

        response = requests.get(
            url=f'{GET_USER_URL}/{create_user["username"]}',
            headers={"accept": "application/json"}
        )

        jsn1 = response.json()

        assert response.status_code == 404
        assert jsn1["message"] == 'User not found'
