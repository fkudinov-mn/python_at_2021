import pytest

from tests.osokolov.api_client import ApiClientBookStore


@pytest.fixture(scope='session')
def get_user():
    login = 'osok'
    password = 'Qwerty!23'
    user = ApiClientBookStore(login, password)
    yield user


def test_login_user():
    login = 'osok'
    password = 'Qwerty!23'
    user = ApiClientBookStore(login, password).login_user()
    assert user.status_code == 200
    assert user.text == 'true'


def test_add_book(get_user):
    user = get_user
    user.prepare_user()
    isbn = '9781449331818'
    user.add_book(user.user_id, isbn)


def test_token(get_user):
    user = get_user
    user.login_user()
    assert user.generate_token().status_code == 200



