from pipconf.configs import PipConfigs
from unittest.mock import MagicMock, patch
from pytest import mark, raises
from pathlib import Path


HOME_DIRECTORY = '/home/user'
SOME_PATH = Path('/some/path')
SYMLINK_PATH = Path('/home/user/.pip/test.conf')
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
    with raises(EnvironmentError):
        PipConfigs().current


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(side_effect=[True, True]))
@patch('pipconf.configs.Path.readlink', MagicMock(return_value=SYMLINK_PATH))
def test_current():
    configs = PipConfigs()
    assert configs.current == SYMLINK_PATH


@patch('pipconf.configs.Path.cwd', MagicMock(return_value=SOME_PATH))
@patch('pipconf.configs.Path.exists', MagicMock(return_value=False))
def test_local_not_found():
    with raises(EnvironmentError):
        PipConfigs().current


@patch('pipconf.configs.Path.cwd', MagicMock(return_value=SOME_PATH))
@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
def test_local():
    config = PipConfigs()
    assert config.local == SOME_PATH.joinpath('pip.conf')


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
@patch('pipconf.configs.Path.iterdir', MagicMock(return_value=[]))
def test_available_configs_empty():
    with raises(EnvironmentError):
        PipConfigs().available_configs


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
@patch('pipconf.configs.Path.iterdir', MagicMock(return_value=[SOME_PATH]))
@patch('pipconf.configs.Path.is_symlink', MagicMock(return_value=True))
def test_available_configs_empty_cause_of_symlinks():
    with raises(EnvironmentError):
        PipConfigs().available_configs


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
@patch('pipconf.configs.Path.iterdir', MagicMock(return_value=[SOME_PATH]))
@patch('pipconf.configs.Path.is_symlink', MagicMock(return_value=False))
def test_available_configs():
    configs = PipConfigs()
    assert configs.available_configs == [SOME_PATH]


@mark.parametrize(
    ('input_name', 'expected_return'),
    [
        ('file', Path(HOME_DIRECTORY, '.pip/file.conf')),
        ('file.conf', Path(HOME_DIRECTORY, '.pip/file.conf')),
    ],
)
@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
def test_get_path(input_name: str, expected_return: Path):
    configs = PipConfigs()
    assert configs.get_path(input_name) == expected_return


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(return_value=False))
def test_select_path_does_not_exists():
    with raises(EnvironmentError):
        PipConfigs().select(SOME_PATH)


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
@patch('pipconf.configs.Path.is_symlink', MagicMock(return_value=True))
@patch('pipconf.configs.Path.unlink')
@patch('pipconf.configs.Path.symlink_to')
def test_select(symlink_to_mock: MagicMock, unlink_mock: MagicMock):
    PipConfigs().select(SOME_PATH)
    assert symlink_to_mock.call_count == 1
    assert unlink_mock.call_count == 1


@patch('pipconf.configs.Path.home', HOME_MOCK)
@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
@patch('pipconf.configs.Path.is_symlink', MagicMock(return_value=False))
@patch('pipconf.configs.Path.unlink')
@patch('pipconf.configs.Path.symlink_to')
@patch('pipconf.configs.copyfile')
def test_select_backup_original_conf(
    copyfile_mock: MagicMock, symlink_to_mock: MagicMock, unlink_mock: MagicMock
):
    PipConfigs().select(SOME_PATH)
    assert copyfile_mock.call_count == 1
    assert symlink_to_mock.call_count == 1
    assert unlink_mock.call_count == 1


@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
def test_create_path_does_not_exists():
    with raises(EnvironmentError):
        PipConfigs().create(SOME_PATH)


@patch('pipconf.configs.Path.exists', MagicMock(return_value=False))
@patch('pipconf.configs.copyfile')
def test_create(copyfile_mock: MagicMock):
    PipConfigs().create(SOME_PATH)
    assert copyfile_mock.call_count == 1


@patch('pipconf.configs.Path.exists', MagicMock(return_value=False))
def test_show_path_does_not_exists():
    with raises(EnvironmentError):
        PipConfigs().show(SOME_PATH)


@patch('pipconf.configs.Path.exists', MagicMock(return_value=True))
@patch('pipconf.configs.Path.read_text')
def test_show(read_text_mock: MagicMock):
    read_text_mock.return_value = 'some content'
    config = PipConfigs()
    assert config.show(SOME_PATH) == 'some content'
