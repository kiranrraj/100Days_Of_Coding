# Title  : Dictionary examples
# Author : Kiran raj R.
# Date   : 23:10:2020

dict1 = {1: 10, 2: 20}
dict2 = {'a': 'apple', 'b': 'ball'}
dict3 = {}

for d in (dict1, dict2):
    dict3.update(d)

print(dict3)


def find_key(dict_in, key_in):
    if key_in in list(dict_in):
        print(f"Key {key_in} available in {dict_in}")


find_key({1: 10, 2: 20, 3: 30, 4: 40, 5: 50}, 1)
find_key({1: 10, 2: 20, 3: 30, 4: 40, 5: 50}, 3)
find_key({1: 10, 2: 20, 3: 30, 4: 40, 5: 50}, 10)


def create_dict(num):
    newDict = {}
    for i in range(1, 11):
        newDict[i] = num*i
    print(f"The newly created dictionary : {newDict}")
    print(f"Sum of values is {sum(newDict.values())}")


create_dict(11)


def find_max_min(dict_in):
    print(dict_in.keys())
    max_key = max(dict_in.keys(), key=(lambda k: dict_in[k]))
    min_key = min(dict_in.keys(), key=(lambda k: dict_in[k]))
    print(min_key, max_key)


find_max_min({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 22: 1, 10: 10, 6: 200})


numDict = {'a': [33, 21, 200, 100, 20], 'b': [
    12, 89, 56, 23, 78, 11], 'c': [88, 44, 71, 23, 90, 22, 10]}

sorted_dict = {x: sorted(y) for x, y in numDict.items()}
print(sorted_dict)
