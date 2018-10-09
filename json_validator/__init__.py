import fastjsonschema


def validate(data, schema):
    try:
        validate_entry = fastjsonschema.compile(schema)
    except fastjsonschema.JsonSchemaDefinitionException as e:
        raise e
    errors = []
    correct = []

    for obj in data:
        try:
            new_data = validate_entry(obj)
        except fastjsonschema.JsonSchemaException as e:
            errors.append({
                "error": e.message,
                "object": obj
            })
        else:
            correct.append(new_data)
    return (correct, errors)
