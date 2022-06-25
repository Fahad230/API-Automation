from client import client
from requests.structures import CaseInsensitiveDict
import requests
import pytest
from config import BASE_URL, TOKEN_BASE_URL


@pytest.fixture(scope='class')
def token():
    payload = {'id': 'xyz', 'user': 'test_user',
            'pass': 'Test@123'}
    response = requests.post(f'{TOKEN_BASE_URL}/a/b/c/d/e-f-g/h', data=payload)
    return "Bearer " + response.json()['auth_token']


@pytest.fixture(scope='class')
def test_fixture(token):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = token
    return client.RequestClient().get_req(f'{BASE_URL}/abc', headers=headers)