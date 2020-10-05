import os
import pytest

import helpers.const as const
from helpers.api import API
from helpers.readers import read_yaml

config = read_yaml(os.path.join(const.PROJECT, 'config.yaml'))
api_url = config['api_url']
api = API(api_url)


def pytest_make_parametrize_id(val):
    return repr(val)


@pytest.fixture()
def delete_all_templates():
    templates = api.get_templates().json()["templates"]
    for name in templates:
        api.delete_template(name)


@pytest.fixture()
def upload_test_templates():
    for num in range(1, 5):
        name = f'{num}.yaml'
        filename = os.path.join(const.TEST_DATA, name)
        api.upload_template(filename=filename)
