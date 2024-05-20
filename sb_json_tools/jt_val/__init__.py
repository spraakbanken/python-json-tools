"""Module to validate json object according to a json-schema.org schema."""

import fastjsonschema  # type: ignore

from typing import Dict
from typing import Generator
from typing import Iterable
from typing import List
from typing import Tuple
from typing import Union

from . import exceptions


__version__ = "0.1.0"


def ok(item: Dict) -> Tuple[Dict, None]:
    """Create a valid item.

    >>> ok({'a':'b'})
    ({'a': 'b'}, None)

    Args:
        item (Dict): The valid item

    Returns:
        Tuple[Dict, None]: a tuple (item, None)
    """
    return (item, None)


def error(item: Dict, msg: str) -> Tuple[None, Dict]:
    """Create an error.

    >>> error({'a':'b'}, 'msg')
    (None, {'failing': {'a': 'b'}, 'message': 'msg'})

    Args:
        item (Dict): the failing item
        msg (str): error message

    Returns:
        Tuple[None, Dict]: a tuple of (None, ErrorDict)
    """
    return (None, {"failing": item, "message": msg})


def streaming_validate(
    schema: Dict, data: Union[Dict, Iterable[Dict]], *, raise_on_error: bool = False
) -> Generator[Union[Tuple[Dict, None], Tuple[None, Dict]], None, None]:
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
    errors: List[Dict] = []
    correct: List[Dict] = []

    for ok_, error_ in streaming_validate(schema, data, raise_on_error=raise_on_error):
        if ok_:
            correct.append(ok_)
        elif error_:
            errors.append(error_)
    return correct, errors


def processing_validate(
    schema: Dict,
    data: Union[Dict, Iterable[Dict]],
    *,
    on_ok: Generator[None, Dict, None],
    on_error: Generator[None, Dict, None],
) -> None:
    for ok_, error_ in streaming_validate(schema, data):
        if ok_:
            on_ok.send(ok_)
        elif error_:
            on_error.send(error_)
