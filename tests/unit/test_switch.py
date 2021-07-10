from unittest.mock import patch
from pytest import mark
from pipconf import switch

from tests.fixtures.switch import UserPathMock
from tests.fixtures.switch import USER_PIP_CONFIG_FILE
from tests.fixtures.switch import GET_CURRENT_CONFIGURATION


@mark.parametrize('absolute_path_return,filename_return', GET_CURRENT_CONFIGURATION)
@patch('pipconf.switch.os.path.basename')
@patch('pipconf.switch.os.path.realpath')
def test_get_current_configuration_sucess(get_absolute_path, get_filename, absolute_path_return, filename_return):
    get_absolute_path.return_value = absolute_path_return
    get_filename.return_value = filename_return
    filename, absolute_path = switch.get_current_configuration()
    assert filename == filename_return
    assert absolute_path == absolute_path_return

@patch('pipconf.switch.os.path.realpath')
def test_get_current_configuration_exception(get_absolute_path):
    get_absolute_path.side_effect = FileNotFoundError()
    filename, absolute_path = switch.get_current_configuration()
    assert filename is None
    assert absolute_path is None

@patch('pipconf.switch.UserPath', UserPathMock)
@patch('pipconf.switch.os.remove')
def test_remove_current_configuration(os_remove):
    switch.remove_current_configuration()
    os_remove.assert_called_once_with(USER_PIP_CONFIG_FILE)

@patch('pipconf.switch.UserPath', UserPathMock)
@patch('pipconf.switch.remove_current_configuration')
@patch('pipconf.switch.os.symlink')
def test_set_current_configuration(os_symlink, remove_config):
    switch.set_current_configuration('')
    remove_config.assert_called_once_with()
    os_symlink.assert_called_once_with('', USER_PIP_CONFIG_FILE)