from pathlib import Path
from shutil import copyfile
from typing import List, Optional


class PipConfigs:
    def __init__(self) -> None:
        self._directory: Optional[Path] = None
        self._default_file: Optional[Path] = None
        self._extension = 'conf'
        self._config_file = 'pip.conf'
        self._template = Path(__file__).parent.joinpath(
            f'templates/{self._config_file}'
        )

    @property
    def directory(self) -> Path:
        if self._directory is None:
            self._directory = Path.home().joinpath('.pip')
            if not self._directory.exists():
                self._directory.mkdir(exist_ok=True)
        return self._directory

    @property
    def default_file(self) -> Path:
        if self._default_file is None:
            self._default_file = self.directory.joinpath(self._config_file)
        return self._default_file

    @property
    def current(self) -> Path:
        if not self.default_file.exists():
            raise EnvironmentError('No configuration found!')
        return self.default_file.readlink()

    @property
    def local(self) -> Path:
        cwd = Path.cwd()
        file_path = cwd.joinpath(self._config_file)
        if not file_path.exists():
            raise EnvironmentError(f'No configuration found at {str(cwd)}!')
        return file_path

    @property
    def available_configs(self) -> List[Path]:
        gotten_files = [
            path for path in self.directory.iterdir() if not path.is_symlink()
        ]
        if not gotten_files:
            raise EnvironmentError('No one configuration found!')
        return gotten_files

    def get_path(self, name: str) -> Path:
        if not name.endswith(self._extension):
            name = f'{name}.{self._extension}'
        return self.directory.joinpath(name)

    def select(self, path: Path):
        if not path.exists():
            raise EnvironmentError(f'The file {path} does not exist!')
        if all(
            [self.default_file.exists(), not self.default_file.is_symlink()]
        ):
            backup_path = self.default_file.parent.joinpath(
                f'pip.backup.{self._extension}'
            )
            copyfile(self.default_file, backup_path)
        self.default_file.unlink(missing_ok=True)
        self.default_file.symlink_to(path)

    def create(self, path: Path):
        if path.exists():
            raise EnvironmentError(f'The file {path} already exists!')
        copyfile(self._template, path)

    def show(self, path: Path) -> str:
        if not path.exists():
            raise EnvironmentError(f'The file {path} does not exist!')
        return path.read_text()
