from pathlib import Path
from shutil import copyfile
from typing import List, Optional


class PipConfigurations:

    def __init__(self) -> None:
        self._directory: Optional[Path] = None
        self._default_file: Optional[Path] = None
        self._extension = 'conf'

    def _conf_name(self, path: Path) -> str:
        return path.name.removesuffix(f'.{self._extension}')

    def _conf_file(self, name: str) -> Path:
        return self.directory.joinpath(f'{name}.{self._extension}')

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
            self._default_file = self.directory.joinpath(f'pip.{self._extension}')
        return self._default_file
    
    @property
    def current(self) -> Optional[str]:
        if self.default_file.exists():
            return self._conf_name(self.default_file.readlink())
        return None
    
    @property
    def available_configs(self) -> List[str]:
        return [
            self._conf_name(path)
            for path in self.directory.iterdir()
            if all([
                not path.is_symlink(),
                path != self.default_file
            ])
        ]

    def select(self, name: str):
        if self.default_file.exists():
            if self.default_file.is_symlink():
                self.default_file.unlink()
            else:
                backup_path = self.default_file.parent.joinpath(f'pip.backup.{self._extension}')
                copyfile(str(self.default_file), str(backup_path))
        self.default_file.symlink_to(str(self._conf_file(name)))
    
    def create(self, name: str) -> Path:
        config_path = self._conf_file(name)
        if config_path.exists():
            raise EnvironmentError(
                f'The file {name}.conf already exists on {str(self.directory)}!'
            )
        config_path.touch()
        return config_path
    
    def show(self, name: str) -> str:
        config_path = self._conf_file(name)
        if not config_path.exists():
            raise EnvironmentError(
                f'The file {name}.conf does not exist on {str(self.directory)}!'
            )
        with open(config_path, 'r') as file:
            return file.read()
        