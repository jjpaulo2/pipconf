from pipconf.configs import PipConfigs
from unittest.mock import MagicMock, patch
from pytest import raises
from pathlib import Path

HOME_DIRECTORY = '/home/user'
SYMLINK_PATH = '/home/user/.pip/test.conf'
HOME_MOCK = MagicMock(return_value=Path(HOME_DIRECTORY))


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
def test_directory_exists():
    configs = PipConfigs()
    expected_value = Path(HOME_DIRECTORY).joinpath('.pip')
    assert configs.directory == expected_value


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(return_value=False))
@patch('pipconf.configs.Path.mkdir')
def test_directory_does_not_exists(mkdir: MagicMock):
    configs = PipConfigs()
    expected_value = Path(HOME_DIRECTORY).joinpath('.pip')
    assert configs.directory == expected_value
    assert mkdir.call_count == 1


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
def test_default_file():
    configs = PipConfigs()
    expected_value = Path(HOME_DIRECTORY).joinpath('.pip/pip.conf')
    assert configs.default_file == expected_value


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(side_effect=[True, False]))
def test_current_file_not_found():
    configs = PipConfigs()
    with raises(EnvironmentError):
        configs.current


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(side_effect=[True, True]))
@patch('pipconf.configs.Path.readlink')
def test_current(readlink: MagicMock):
    readlink.return_value = Path(SYMLINK_PATH)
    configs = PipConfigs()
    assert configs.current == Path(SYMLINK_PATH)
    assert readlink.call_count == 1

