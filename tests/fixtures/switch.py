from enum import Enum

class UserPathMock(Enum):
    PIP_CONFIG_DIRECTORY = '/path/to/pip/config'


USER_PIP_CONFIG_FILE = UserPathMock.PIP_CONFIG_DIRECTORY.value + '/pip.conf'

GET_CURRENT_CONFIGURATION = [
    ('/path/to/my/file.conf', 'file.conf')
]
