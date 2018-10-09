import fastjsonschema


def validate(data, schema):
    try:
        validate_entry = fastjsonschema.compile(schema)
    except fastjsonschema.JsonSchemaDefinitionException as e:
        raise e

    data_passing = []
    data_failing = []
    stats = { 'total': 0, 'failing': 0}
    for obj in data:
        try:
            new_data = validate_entry(obj)
        except fastjsonschema.JsonSchemaException as e:
            data_failing.append({})
