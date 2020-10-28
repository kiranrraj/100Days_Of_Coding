# Title  : Merge dictionaries into one
# Author : Kiran raj R.
# Date   : 28:10:2020

dict1 = {"fname": "kiran", "lname": "raj", "initials": "r"}
dict2 = {"mobile": True, "laptop": True}

new_dict = {**dict1, **dict2}
print(new_dict)
