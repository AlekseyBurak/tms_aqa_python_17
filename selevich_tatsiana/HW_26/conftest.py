import pytest
import requests
from URLs import URL
from mock_data import FIRST_USER_PAYLOAD


@pytest.fixture
def create_user():
    payload = FIRST_USER_PAYLOAD

    requests.post(
        url=f'{URL}user',
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json=payload
    )

    yield payload

    requests.delete(
        url=f'{URL}user/{FIRST_USER_PAYLOAD["username"]}'
    )
