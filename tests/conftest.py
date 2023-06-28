import pytest as pytest

from python_yapi import YApi


@pytest.fixture(scope='session')
def base_url():
    return 'http://localhost:3001'


@pytest.fixture(scope='session')
def user():
    return 'admin@admin.com', 'ymfe.org'


@pytest.fixture(scope='session')
def yapi(base_url, user):
    yapi = YApi(base_url)
    yapi.login(*user)
    return yapi
