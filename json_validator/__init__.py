import fastjsonschema


def validate(schema, data):
    v = fastjsonschema.compile(schema)
    errors = []
    correct = []
    
    for obj in data:
#        print(json.dumps(obj))
        try:
            new_data = v(obj)
        except fastjsonschema.JsonSchemaException as e:
            errors.append({
                "error": e.message,
                "object": obj
            })
        else:
            correct.append(new_data)
    return (correct, errors)
    