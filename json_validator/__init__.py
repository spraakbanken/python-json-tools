import fastjsonschema


def validate(schema, data):
    v = fastjsonschema.compile(schema)
    errors = {}
    correct = []
    error_id = 0
    
    for obj in data:
#        print(json.dumps(obj))
        try:
            new_data = v(obj)
        except fastjsonschema.JsonSchemaException as e:
            errors[error_id] = {
                "error": e.message,
                "object": obj
            }
            correct.append({"error_id": error_id})
            error_id += 1
        else:
            correct.append(new_data)
    return (correct, errors)
