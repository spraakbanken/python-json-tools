import os
import sys
import click

from jt_iter import jsonlib
from jt_val import validate
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
    click.echo("Validating {0} with the schema in {1}.".format(infile, schema))
    schema_json = jsonlib.load_from_file(schema)
    data = jt_iter.load_from_file(infile)
    correct, errors = validate(schema_json, data)
    jiter.dump_to_file(correct, outfile)
    if not errors:
        click.echo("No errors!")
    else:
        (out_root, out_ext) = os.path.splitext(outfile)
        errors_filename = os.path.join(out_root, ".errors", out_ext)
        jt_iter.dump_to_file(errors, errors_filename)
        click.echo("ERRORs found!!!")
        click.echo("Errors are written to {0}".format(errors_filename))
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
