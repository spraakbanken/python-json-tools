import sys

import click

import json_streams
from json_streams import jsonlib

from sb_json_tools import jt_val


__version__ = "0.5.2"


@click.group()
def cli():
    pass


@cli.command()
@click.option("--schema", "-s", help="Schema to use for validating.")
@click.argument("infile", type=click.File("br"))
@click.argument("outfile", type=click.File("bw"))
def validate(infile, outfile, schema):
    """Validates a json-file with a schema (json-schema.org)."""
    # click.echo("Validating {0} with the schema in {1}.".format(infile, schema))
    schema_json = jsonlib.load_from_file(schema)
    data = json_streams.load(infile)
    correct, errors = jt_val.validate(schema_json, data)
    json_streams.dump(correct, outfile)
    if errors:
        # (out_root, out_ext) = os.path.splitext(outfile)
        # errors_file_name = os.path.join(out_root, ".errors", out_ext)
        json_streams.dump(errors, sys.stderr)
        # click.echo("ERRORs found!!!")
        # click.echo("Errors are written to {0}".format(errors_file_name))
        click.Context.exit(len(errors))


@cli.command()
@click.argument("src", type=click.File("br"))
@click.argument("dst", type=click.File("bw"))
def convert(src, dst):
    json_streamsdump(json_streams.load(src), dst)


if __name__ == "__main__":
    cli()
