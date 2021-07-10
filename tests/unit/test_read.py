from unittest.mock import patch
from pytest import mark
from pipconf import read

from tests.fixtures.read import CONFIGURATION_FILE_FILTER
from tests.fixtures.read import GET_CONFIGURATION_FILES
from tests.fixtures.read import GET_USER_CONFIGURATION_FILES
from tests.fixtures.read import GET_LOCAL_CONFIGURATION_FILES


@mark.parametrize('filename,expected', CONFIGURATION_FILE_FILTER)
def test_configuration_files_filter(filename, expected):
    is_conf_file = read.configuration_files_filter(filename)
    assert is_conf_file == expected

@mark.parametrize('listdir_return,expected', GET_CONFIGURATION_FILES)
@patch('pipconf.read.os.listdir')
def test_get_configuration_files_sucess(listdir, listdir_return, expected):
    listdir.return_value = listdir_return
    config_files = read.get_configuration_files('')
    assert config_files == expected

@patch('pipconf.read.os.listdir')
def test_get_configuration_files_exception(listdir):
    listdir.side_effect = FileNotFoundError()
    config_files = read.get_configuration_files('')
    assert config_files == []

@mark.parametrize('config_files_return,expected', GET_USER_CONFIGURATION_FILES)
@patch('pipconf.read.get_configuration_files')
def test_get_user_configuration_files(config_files, config_files_return, expected):
    config_files.return_value = config_files_return
    user_config_files = read.get_user_configuration_files()
    assert user_config_files == expected

@mark.parametrize('config_files_return', GET_LOCAL_CONFIGURATION_FILES)
@patch('pipconf.read.get_configuration_files')
def test_get_local_configuration_files(get_config_files, config_files_return):
    get_config_files.return_value = config_files_return
    config_files = read.get_local_configuration_files()
    assert config_files == config_files_return