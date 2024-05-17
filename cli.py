import click

from utils import transcribe

@click.group()
def cli():
    pass

@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def add(a, b):
    print( a + b)


@cli.command()
@click.argument('src', type=click.File('rb'))
def aud2txt(src):

    click.echo(transcribe(src).text)

if __name__ == '__main__':
    cli()
