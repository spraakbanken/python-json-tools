import json
import os

import click

from json_validator import validate


@click.command()
@click.option('--schema', '-s', type=click.File('r'),
                                        help='Schema to use for validating.')
@click.argument('infile', required=True, type=click.File('r'))
@click.argument('outfile', required=True, type=click.File('w'))
def main(infile, outfile, schema):
    """Validates a json-file with a schema (json-schema.org)."""
    click.echo('Validating {0} with the schema in {1}.'.format(infile, schema))
    schema_json = json.load(schema)
    data = json.load(infile)
    correct, errors = validate(schema_json, data)
    json.dump(correct, outfile)
    if not errors:
        click.echo('No errors!')
    else:
        errors_filename = os.path.join(outfile.name, '.errors')
        with open(errors_filename) as errors_file:
            json.dump(errors, errors_file)
        click.echo('ERRORs found!!!')
        click.echo('Errors are written to {0}'.format(errors_filename))
        click.Context.exit(len(errors))
