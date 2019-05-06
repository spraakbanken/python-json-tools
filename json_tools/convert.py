import click

from json_tools.iter import load_from_file
from json_tools.iter import dump_to_file


def convert_json(
        in_file: str,
        out_file: str
        ):
    dump_to_file(
        load_from_file(in_file),
        out_file
    )


@click.group()
def cli():
    pass


@cli.command()
@click.argument('src')
@click.argument('dst')
def convert(src, dst):
    convert_json(src, dst)


if __name__ == '__main__':
    cli()
