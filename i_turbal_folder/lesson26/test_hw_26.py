import allure
import pytest
import requests
import json

URL = 'https://petstore.swagger.io/v2/'

user_request = {
    "id": 0,
    "username": "tuhtick",
    "firstName": "Tukhtasun",
    "lastName": "Ekaterinovich",
    "email": "tukhta@best.cat",
    "password": "meow",
    "phone": "+375222222233",
    "userStatus": 0
}


class TestUser:
    @allure.title('Create user')
    def test_post_user(self):
        post_response = requests.post(
            url=f'{URL}user',
            headers={"accept": "application/json",
                     "Content-Type": "application/json"},
            json=user_request
        )
        assert post_response.status_code == 200

    @allure.title("Check created user")
    def test_get_user(self):
        get_response = requests.get(
            url=f'{URL}user/tuhtick',
            headers={"accept": "application/json",
                     "Content-Type": "application/json"},
        )
        jsn = get_response.json()
        assert  get_response.status_code == 200
        for key in user_request.keys():
            if key != 'id':
                assert user_request[key] == jsn[key]

    @allure.title("test update email")
    def test_user_put(self):
        with allure.step("Update email"):
            update_user_email  = user_request.copy()
            update_user_email["email"] = 'saf@sadf.com'
        put_response = requests.put(
            url=f'{URL}user/tuhtick',
            headers = {"accept": "application/json",
                   "Content-Type": "application/json"},
            json= update_user_email
        )

        assert put_response.status_code == 200
        with allure.step('Get changed user'):
            get_response = requests.get(
                url=f'{URL}user/tuhtick',
                headers={"accept": "application/json",
                         "Content-Type": "application/json"},
            )
            jsn = get_response.json()
        assert update_user_email['email'] == jsn['email']

    def test_login_user(self):
        login_response = requests.get(
            url=f'{URL}user/login',
            headers = {"accept": "application/json"},
            params = {"username": "tuhtick",
                  "password": "meow"}
        )
        jsn = login_response.json()
        assert login_response.status_code == 200
        assert "logged in user session" in jsn['message']

    def test_logout_user(self):
        logout_response = requests.get(
            url=f'{URL}logout',
            headers={"accept": "application/json"},
        )
        assert logout_response.status_code == 404

    @pytest.mark.xfail
    def test_invalid_password(self):
        login_response = requests.get(
            url=f'{URL}user/login',
            headers={"accept": "application/json"},
            params={"username": "tuhtick",
                    "password": "123"}
        )
        jsn = login_response.json()
        assert login_response.status_code == 400


    def test_delete_user(self):
        delete_response = requests.delete(
            url=f"{URL}user/tuhtick",
            headers={"accept": "application/json"},
        )
        assert delete_response.status_code == 200
        get_response = requests.get(
            url=f'{URL}user/tuhtick',
            headers={"accept": "application/json",
                     "Content-Type": "application/json"},
        )
        assert get_response.status_code == 404











