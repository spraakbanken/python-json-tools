import json

import click

from json_validator import get_validator

@click.command()
@click.option('--schema', '-s', type=click.File('r'), help='Schema to use for validating.')
@click.argument('file', default='world', required=True, type=click.File('r'))
def main(file, schema):
    """Validates a json-file with a schema (json-schema.org)."""

    click.echo('Validating {0} with the schema in {1}.'.format(file, schema))
    validator = get_validator(schema)
    data = json.load(file)
    validator.validate(data)
