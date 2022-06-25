from pytest_bdd import *
from config import *
scenarios('../features/ThinkPad.feature')


@given(name='the endpoint of Thinkpads after the base URL', converters=None, target_fixture='Thinking')
def given_ThinkPad(test_fixture):
    assert (f'{BASE_URL}/abc') == test_fixture.url


@when(name='the GET request sent with header and token', converters=None, target_fixture='Thinking')
def when_ThinkPad(test_fixture):
    assert test_fixture.ok


@then(name='the response code should be 200 with the valid response body data', converters=None, target_fixture='Thinking')
def then_ThinkPad(test_fixture):
    assert test_fixture.status_code == 200
    assert test_fixture.json() != None


