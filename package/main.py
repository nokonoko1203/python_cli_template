from .settings import SAMPLE_STATES
from .sample_module import sample_function


def core() -> None:
    print(f"{SAMPLE_STATES=}")
    print(f"sample_function={sample_function()}")


if __name__ == '__main__':
    core()
