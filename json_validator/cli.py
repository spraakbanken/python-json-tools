import json

import click

import json_validator

@click.command()
@click.option('--schema', '-s', type=click.File('r'), help='Schema to use for validating.')
@click.argument('file_in', required=True, type=click.File('r'))
@click.argument('file_out', required=True, type=click.File('w'))
def main(file_in, file_out, schema):
    """Validates a json-file with a schema (json-schema.org)."""

#    click.echo('Validating {0} with the schem8a88 in {1}.'.format(file, schema))
    schema_json = json.load(schema)
    data = json.load(file_in)
    
    correct, errors = json_validator.validate(schema_json, data)
    json.dump(correct, file_out)
    if errors:
        print(json.dumps(errors))
