import json


json_string = input()

py_obj = json.loads(json_string)

print(type(py_obj), py_obj, sep="\n")