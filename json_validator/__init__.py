"""Module to validate json object according to a json-schema.org schema."""

import fastjsonschema

from json_validator.exceptions import JsonValidatorSchemaDefinitionException


def validate(data, schema):
    try:
        validate_entry = fastjsonschema.compile(schema)
    except fastjsonschema.JsonSchemaDefinitionException as e:
        raise JsonValidatorSchemaDefinitionException(e.message)

    errors = []
    error_id = 0
    correct = []

    for obj in data:
        try:
            new_data = validate_entry(obj)
        except fastjsonschema.JsonSchemaException as e:
            errors.append({
                "error_id": error_id,
                "error": e.message,
                "object": obj
            })
            correct.append({"_JSON_VALIDATOR_ERROR_ID": error_id})
            error_id += 1
        else:
            correct.append(new_data)
    return (correct, errors)
