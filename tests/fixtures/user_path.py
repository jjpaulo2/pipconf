from enum import Enum

class UserPathMock(Enum):
    PIP_CONFIG_DIRECTORY = '/path/to/pip/config'

USER_PIP_CONFIG_FILE = UserPathMock.PIP_CONFIG_DIRECTORY.value + '/pip.conf'
USER_PIP_CONFIG_FOLDER = UserPathMock.PIP_CONFIG_DIRECTORY.value