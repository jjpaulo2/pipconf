from unittest.mock import patch
from pytest import mark
from pipconf import kernel

from tests.fixtures.user_path import UserPathMock
from tests.fixtures.user_path import USER_PIP_CONFIG_FOLDER
from tests.fixtures.kernel import USER_CONFIGURATION_FILES
from tests.fixtures.kernel import USER_CONFIGURATION_FILEPATHS
from tests.fixtures.kernel import SET_USER_CONFIGURATION
from tests.fixtures.kernel import GET_LOCAL_CONFIGURATION_FILES_SUCESS
from tests.fixtures.kernel import GET_LOCAL_CONFIGURATION_FILES_FAIL


@patch('pipconf.kernel.UserPath', UserPathMock)
@patch('pipconf.read.get_user_configuration_files')
def test_get_user_configurations(get_user_config_files, USER_CONFIGURATION_FILES, USER_CONFIGURATION_FILEPATHS):
    get_user_config_files.return_value = USER_CONFIGURATION_FILES
    filenames, filepaths = kernel.get_user_configurations()
    assert filenames == USER_CONFIGURATION_FILES
    assert filepaths == USER_CONFIGURATION_FILEPATHS 

@mark.parametrize('file,filepath', SET_USER_CONFIGURATION)
@patch('pipconf.kernel.UserPath', UserPathMock)
@patch('pipconf.switch.set_current_configuration')
def test_set_user_configuration(set_current_configuration, file, filepath):
    kernel.set_user_configuration(file)
    set_current_configuration.assert_called_once_with(filepath)

@mark.parametrize('files', GET_LOCAL_CONFIGURATION_FILES_SUCESS)
@patch('pipconf.switch.set_current_configuration')
@patch('pipconf.kernel.os.getcwd')
@patch('pipconf.read.get_local_configuration_files')
def test_set_local_configuration_sucess(get_local_configuration_files, os_getcwd, set_current_configuration, files):
    get_local_configuration_files.return_value = files
    os_getcwd.return_value = ''
    kernel.set_local_configuration()
    set_current_configuration.assert_called_once_with('/pip.conf')

@mark.parametrize('files', GET_LOCAL_CONFIGURATION_FILES_FAIL)
@patch('pipconf.switch.set_current_configuration')
@patch('pipconf.kernel.os.getcwd')
@patch('pipconf.read.get_local_configuration_files')
def test_set_local_configuration_fail(get_local_configuration_files, os_getcwd, set_current_configuration, files):
    get_local_configuration_files.return_value = files
    kernel.set_local_configuration()
    os_getcwd.assert_not_called()
    set_current_configuration.assert_not_called()