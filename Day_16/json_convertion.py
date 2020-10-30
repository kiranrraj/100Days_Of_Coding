# Title  : Json in python
# Author : Kiran raj R.
# Date   : 29:10:2020

import json

json_data = '{"fName":"Sachin", "lName":"Tendulkar", "Profession":"Cricketer"}'
python_data = json.loads(json_data)
print("-" * 100)
print(f"Output of {json_data} after json.loads is \n{python_data}")
print(f"Type of the out from json loads {type(python_data)}")
print("-" * 100)

json_data = json.dumps(python_data)
print(f"Normal json dumps output {json_data}")
print("*" * 100)

print("json dumps output after applying sort_keys=True, indent=4 ")
print(json.dumps(python_data, sort_keys=True, indent=4))
print(f"Type of the out from json dumps {type(json_data)}")
print("*" * 100)

duplicate = '{"a":  10, "b":  20, "d": "dog","a": 30, "a": 40, "b": 11, "b": 21, "c": "cat"}'
print(f"Only unique keys : {json.loads(duplicate)}")
print("*" * 100)
