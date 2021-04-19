import click

from .settings import SAMPLE_STATES
from .utils import sample_function


@click.command()
@click.argument("param", type=str)
def core(param: str) -> None:
    print(f"{param=}")
    print(f"{SAMPLE_STATES=}")
    print(f"sample_function={sample_function()}")


if __name__ == '__main__':
    core()
