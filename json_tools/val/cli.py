import os
import sys
import click

from json_tools import jsonlib
from json_tools.val import validate
import json_tools.iter as jiter


@click.command()
@click.option("--schema", "-s", help="Schema to use for validating.")
@click.argument("infile", type=click.File('r'))
@click.argument("outfile", type=click.File('w'))
def main(infile, outfile, schema):
    """Validates a json-file with a schema (json-schema.org)."""
    click.echo("Validating {0} with the schema in {1}.".format(infile, schema))
    schema_json = jsonlib.load_from_file(schema)
    data = jiter.load_from_file(infile)
    correct, errors = validate(schema_json, data)
    jiter.dump_to_file(correct, outfile)
    if not errors:
        click.echo("No errors!")
    else:
        (out_root, out_ext) = os.path.splitext(outfile)
        errors_filename = os.path.join(out_root, ".errors", out_ext)
        jiter.dump_to_file(errors, errors_filename)
        click.echo("ERRORs found!!!")
        click.echo("Errors are written to {0}".format(errors_filename))
        click.Context.exit(len(errors))


if __name__ == '__main__':
    main()
