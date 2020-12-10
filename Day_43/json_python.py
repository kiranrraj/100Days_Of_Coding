string_json = '{ "name" : "Kiran", "email" : "kiran@gmail.com", "isHappy": "Yes"}'

import json

json_data = json.loads(string_json)
print(json_data)

python_json = {"name":"kiran", "email":"kiran@gmail.com", "isHappy": "Yes"}
import json
string_j = json.dumps(python_json)
print(string_j)