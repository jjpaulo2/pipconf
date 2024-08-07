from typer import Typer, Exit, launch
from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
from rich.padding import Padding
from pipconf.configs import PipConfigs
from pipconf.consts import PADDING, ExitCodes, Chars


app = Typer()
console = Console()
configs = PipConfigs()


@app.command()
def list():
    """Lists all available configs"""
    try:
        lines = []
        for path in configs.available_configs:
            if path != configs.current:
                lines.append(
                    f"{Chars.EMPTY_CIRCLE.decode()} {path.name} ([grey42]{str(path)}[/])"
                )
            else:
                lines.append(
                    f"[green]{Chars.FILLED_CIRCLE.decode()} {path.name}[/] ([grey42]{str(path)}[/])"
                )

        console.print(Padding(f'Available configurations at [yellow]{configs.directory}[/]:', PADDING))
        console.print(Padding('\n'.join(lines), (0,0,1,1,)))

    except EnvironmentError as exc:
        console.print(Padding(str(exc), PADDING), style='red')
        raise Exit(ExitCodes.NO_SUCH_FILE_OR_DIRECTORY)
        

@app.command()
def current():
    """Shows the currently active config file"""
    try:
        console.print(Padding(
            f'Current configuration is [yellow]{str(configs.current)}[/]!',
            PADDING
        ))

    except EnvironmentError as exc:
        console.print(Padding(str(exc), PADDING), style='red')
        raise Exit(ExitCodes.NO_SUCH_FILE_OR_DIRECTORY)


@app.command()
def new(name: str, open: bool = False):
    """Creates a new config file"""
    try:
        path = configs.get_path(name)
        configs.create(path)
        console.print(Padding(
            f'Config file [green]{path.name}[/] created!',
            PADDING
        ))

        if open:
            launch(str(path), locate=True)

    except EnvironmentError as exc:
        console.print(Padding(str(exc), PADDING))
        raise Exit(ExitCodes.FILE_EXISTS)


@app.command()
def set(name: str):
    """Select a configuration"""
    try:
        path = configs.get_path(name)
        configs.select(path)
        console.print(Padding(
            f'Configuration is now set to [yellow]{path.name}[/]!',
            PADDING
        ))

    except EnvironmentError as exc:
        console.print(Padding(str(exc), PADDING))
        raise Exit(ExitCodes.NO_SUCH_FILE_OR_DIRECTORY)


@app.command()
def show(name: str):
    """Shows a config file content"""
    try:
        path = configs.get_path(name)
        console.print(Panel(
            Syntax(configs.show(path), 'ini'),
            title=str(path)
        ))

    except EnvironmentError as exc:
        console.print(Padding(str(exc), PADDING))
        raise Exit(ExitCodes.NO_SUCH_FILE_OR_DIRECTORY)


@app.command()
def local():
    """Select a config file in current workdir"""
    try:
        local_config = configs.local
        configs.select(local_config)
        console.print(Padding(
            f'Configuration is now set to [yellow]{str(local_config)}[/]!',
            PADDING
        ))

    except EnvironmentError as exc:
        console.print(Padding(str(exc), PADDING))
        raise Exit(ExitCodes.NO_SUCH_FILE_OR_DIRECTORY)
