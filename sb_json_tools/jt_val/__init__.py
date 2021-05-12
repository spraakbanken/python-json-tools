"""Module to validate json object according to a json-schema.org schema."""

import fastjsonschema

from typing import Dict, Optional
from typing import Generator
from typing import Iterable
from typing import List
from typing import Tuple
from typing import Union

from . import exceptions


__version__ = "0.1.0"


def ok(item: Dict) -> Tuple[Dict, None]:
    return (item, None)


def error(item: Dict, msg: str) -> Tuple[None, Dict]:
    return (None, {"failing": item, "message": msg})


def streaming_validate(
    schema: Dict, data: Union[Dict, Iterable[Dict]], *, raise_on_error: bool = False
) -> Generator[Tuple[Optional[Dict], Optional[Dict]], None, None]:
    try:
        validator = fastjsonschema.compile(schema)
    except fastjsonschema.JsonSchemaDefinitionException as e:
        raise exceptions.SchemaDefinitionException(str(e)) from e

    if isinstance(data, dict):
        try:
            valid_obj = validator(data)
            # yield ok(valid_obj)
        except fastjsonschema.JsonSchemaException as e:
            if raise_on_error:
                raise exceptions.ValidationException(str(e), data) from e
            yield error(data, str(e))
        else:
            yield ok(valid_obj)
    else:
        for orig_obj in data:
            try:
                valid_obj = validator(orig_obj)
            except fastjsonschema.JsonSchemaException as e:
                if raise_on_error:
                    raise exceptions.ValidationException(str(e), orig_obj) from e
                yield error(orig_obj, str(e))
            else:
                yield ok(valid_obj)


def validate(
    schema: Dict, data: Union[Dict, Iterable[Dict]], *, raise_on_error: bool = False
) -> Tuple[List[Dict], List[Dict]]:
    errors = []
    correct = []

    for ok, error in streaming_validate(schema, data, raise_on_error=raise_on_error):
        if ok:
            correct.append(ok)
        else:
            errors.append(error)
    return correct, errors


def processing_validate(
    schema: Dict,
    data: Union[Dict, Iterable[Dict]],
    *,
    on_ok: Generator[None, Dict, None],
    on_error: Generator[None, Dict, None]
) -> None:
    for ok, error in streaming_validate(schema, data):
        if ok:
            on_ok.send(ok)
        else:
            on_error.send(error)
