# Title  : Json Module Module
# Author : Kiran Raj R.
# Date   : 26/11/2020

string_json = '{ "name" : "Kiran", "email" : "kiran@gmail.com", "isHappy": "Yes"}'

import json

json_data = json.loads(string_json)
print(json_data)

