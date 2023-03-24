import sys
import click
from pathlib import Path


def get_words(in_text: str) -> list:
    words = in_text.split()
    return words

@click.command()
@click.option("-c", is_flag=True)
@click.option("-l", is_flag=True)
@click.option("-w", is_flag=True)
@click.option("-m", is_flag=True)
@click.argument("input", type=click.File('rb'), default=sys.stdin)
@click.pass_context
def cli(ctx, m: bool, w: bool, l: bool, c: bool, input):
    """This script works similar to the Unix `wc` command but limited
    """
    filename = ctx.params['input'].name
    if filename == '<stdin>':
        in_text = click.get_binary_stream('stdin').read()
        
        if c:
            click.echo(size)
        elif l:
            click.echo(str(len(in_text.splitlines())))
        elif w:
            click.echo(str(len(get_words(in_text))))
        elif m:
            click.echo(str(len(in_text)))
        else:
            lines = str(len(in_text.splitlines()))
            words = str(len(get_words(in_text)))
            chars = str(len(in_text))
            click.echo(lines + " " + words + " " + chars)

    else:
        size = str(Path(filename).stat().st_size)
        in_text = input.read()
        if c:
            click.echo(size + " " + filename)
        elif l:
            click.echo(str(len(in_text.splitlines())) + " " + filename)
        elif w:
            click.echo(str(len(get_words(in_text))) + " " + filename)
        elif m:
            click.echo(str(len(in_text)) + " " + filename)
        else:
            lines = str(len(in_text.splitlines()))
            words = str(len(get_words(in_text)))
            chars = str(len(in_text))
            click.echo(lines + " " + words + " " + chars + " " + filename)
