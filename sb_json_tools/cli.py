import sys

import click

from sb_json_tools import jsonlib
from sb_json_tools import jt_val
from sb_json_tools import jt_iter


__version__ = "0.4.0"


@click.group()
def cli():
    pass


@cli.command()
@click.option("--schema", "-s", help="Schema to use for validating.")
@click.argument("infile", type=click.File("r"))
@click.argument("outfile", type=click.File("w"))
def validate(infile, outfile, schema):
    """Validates a json-file with a schema (json-schema.org)."""
    # click.echo("Validating {0} with the schema in {1}.".format(infile, schema))
    schema_json = jsonlib.load_from_file(schema)
    data = jt_iter.load(infile)
    correct, errors = jt_val.validate(schema_json, data)
    jt_iter.dump(correct, outfile)
    if errors:
        # (out_root, out_ext) = os.path.splitext(outfile)
        # errors_file_name = os.path.join(out_root, ".errors", out_ext)
        jt_iter.dump(errors, sys.stderr)
        # click.echo("ERRORs found!!!")
        # click.echo("Errors are written to {0}".format(errors_file_name))
        click.Context.exit(len(errors))


@cli.command()
@click.argument("src", type=click.File("r"))
@click.argument("dst", type=click.File("w"))
def convert(src, dst):
    jt_iter.dump(jt_iter.load(src), dst)


if __name__ == "__main__":
    cli()
