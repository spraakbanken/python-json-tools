"""Module to validate json object according to a json-schema.org schema."""

import fastjsonschema

from json_validator import exceptions


__version__ = '0.1.0'


class Result(object):
    def __init__(self,
                 ok=None,
                 error=None,
                 error_msg=None):
        if ok is not None and error is not None:
            raise ValueError()
        self.ok = ok
        self.error = error
        self.error_msg = error_msg


def ok(item) -> Result:
    return Result(ok=item)


def error(item, msg) -> Result:
    return Result(error=item, error_msg=msg)


def streaming_validate(schema,
                       data,
                       raise_on_error=False):
    try:
        validator = fastjsonschema.compile(schema)
    except fastjsonschema.JsonSchemaDefinitionException as e:
        raise exceptions.SchemaDefinitionException(e.message)

    for obj in data:
        try:
            item = validator(obj)
        except fastjsonschema.JsonSchemaException as e:
            if raise_on_error:
                raise exceptions.ValidationException(e.message)
            yield error(obj, e.message)
        else:
            yield ok(item)


def validate(schema, data, raise_on_error=False):
    errors = []
    correct = []

    for result in streaming_validate(schema, data, raise_on_error):
        if result.ok:
            correct.append(result.ok)
        else:
            errors.append({
                'failing': result.error,
                'message': result.error_msg
            })
    return correct, errors


def processing_validate(schema,
                        data,
                        on_ok,
                        on_error):
    for result in streaming_validate(schema, data):
        if result.ok:
            on_ok.send(result.ok)
        else:
            on_error.send({
                'failing': result.error,
                'message': result.error_msg
            })
