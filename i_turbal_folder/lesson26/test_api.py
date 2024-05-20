import requests

URL = 'https://petstore.swagger.io/v2/'
def test_get_store_inventory():
    response = requests.get(
        url=f'{URL}store/inventory',
        headers={"accept": "application/json"}
    )
    txt = response.text
    jsn = response.json()
    print()
    print(type(txt))
    print(type(jsn))
    assert response.status_code == 200
