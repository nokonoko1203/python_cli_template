import click


@click.group()
def cmd():
    pass


@cmd.command(help='Subcommand argparse CLI')
@click.option('-n', '--name', 'name', type=str, help='your name', required=True)
def name(name):
    click.echo(f"Your name is {name}")


def main():
    cmd()


if __name__ == '__main__':
    main()
