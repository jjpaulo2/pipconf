from typer import Typer, Exit
from rich.console import Console
from rich.syntax import Syntax
from rich.tree import Tree
from rich.panel import Panel
from pipconf.configs import PipConfigurations


app = Typer()
console = Console()
configs = PipConfigurations()


@app.command()
def list():
    """Lists all available configs"""
    tree = Tree(label=f"Available configs at {str(configs.directory)}")
    for config in configs.available_configs:
        tree.add(f"{config}.conf")
    console.print(tree)

@app.command()
def current():
    """Shows the currently active config file"""
    console.print(f'Current configuration is {configs.current}.conf!')

@app.command()
def select(name: str):
    """Select a configuration"""
    configs.select(name)
    console.print(f'Current configuration now is set to {name}.conf!')

@app.command()
def show(name: str):
    """Shows a config file content"""
    try:
        console.print(Panel.fit(
            Syntax(configs.show(name), 'ini'),
            title=f'{name}.conf'
        ))

    except EnvironmentError as exc:
        console.print(exc)
        raise Exit(2)
