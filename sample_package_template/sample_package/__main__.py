import click

from .modules import sample_function
from .setting import SAMPLE_STATES


@click.command()
@click.argument("param", type=str)
def core(param: str) -> None:
    print(f"{param=}")
    print(f"{SAMPLE_STATES=}")
    print(f"sample_function={sample_function()}")


if __name__ == '__main__':
    core()
