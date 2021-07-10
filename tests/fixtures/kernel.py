from pytest import fixture
from .user_path import USER_PIP_CONFIG_FOLDER

@fixture
def USER_CONFIGURATION_FILES():
    return [
        'config1.conf',
        'config2.conf',
        'config3.conf'
    ]

@fixture
def USER_CONFIGURATION_FILEPATHS(USER_CONFIGURATION_FILES):
    return [f'{USER_PIP_CONFIG_FOLDER}/{fn}' for fn in USER_CONFIGURATION_FILES]

SET_USER_CONFIGURATION = [
    ('myconfig', f'{USER_PIP_CONFIG_FOLDER}/myconfig.conf')
]

GET_LOCAL_CONFIGURATION_FILES_SUCESS = [
    (['conf1.conf', 'pip.conf']),
    (['pip.conf'])
]

GET_LOCAL_CONFIGURATION_FILES_FAIL = [
    (['conf1.conf']),
    ([])
]