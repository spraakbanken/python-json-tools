import sys
import json

import json_validator

arg1 = sys.argv[1]
arg2 = sys.argv[2]

with open(arg1) as s, open(arg2) as a:
    schema = json.load(s)
    data = json.load(a)

def _print_array(a):
    print("[")
    for x in a:
        print(json.dumps(x, indent=2))
    print("]")

    
print ("before:")
print (json.dumps(data, indent=2))
new_data, errors = json_validator.validate(schema,data)
print("stats:")
print(" passed: {0}".format(len(new_data)))
print(" errors: {0}".format(len(errors)))
print("after:")
print("new_data = ")
_print_array(new_data)
print("errors = ")
_print_array(errors)