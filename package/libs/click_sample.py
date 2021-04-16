import click


@click.command(help='Simple click CLI')
@click.option('-n', '--name', 'name', type=str, help='your name', required=True)
def main(name):
    print(f"Your name is {name}")


if __name__ == '__main__':
    main()
