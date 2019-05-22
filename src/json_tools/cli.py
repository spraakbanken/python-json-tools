__version__ = '0.2.8'
import sys

import click

from jt_iter import jsonlib
import jt_val
import jt_iter


@click.group()
def cli():
    pass


@cli.command()
@click.option("--schema", "-s", help="Schema to use for validating.")
@click.argument("infile", type=click.File('r'))
@click.argument("outfile", type=click.File('w'))
def validate(infile, outfile, schema):
    """Validates a json-file with a schema (json-schema.org)."""
    # click.echo("Validating {0} with the schema in {1}.".format(infile, schema))
    schema_json = jsonlib.load_from_file(schema)
    data = jt_iter.load(infile)
    correct, errors = jt_val.validate(schema_json, data)
    jt_iter.dump(correct, outfile)
    if errors:
        # (out_root, out_ext) = os.path.splitext(outfile)
        # errors_filename = os.path.join(out_root, ".errors", out_ext)
        jt_iter.dump(errors, sys.stderr)
        # click.echo("ERRORs found!!!")
        # click.echo("Errors are written to {0}".format(errors_filename))
        click.Context.exit(len(errors))


@cli.command()
@click.argument('src', type=click.File('r'))
@click.argument('dst', type=click.File('w'))
def convert(src, dst):
    jt_iter.dump(
        jt_iter.load(src),
        dst
    )


if __name__ == '__main__':
    cli()
