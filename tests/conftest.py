import pytest as pytest

from python_yapi import YApi


@pytest.fixture(scope='session')
def base_url():
    return 'http://localhost:3000'


@pytest.fixture(scope='session')
def admin():
    return 'admin@admin.com', 'ymfe.org'


@pytest.fixture(scope='session')
def yapi(base_url):
    yapi = YApi(base_url)
    return yapi


@pytest.fixture(scope='session')
def yapi_login(yapi, admin):
    yapi.login(*admin)
    return yapi


@pytest.fixture()
def project_id():
    return 11
