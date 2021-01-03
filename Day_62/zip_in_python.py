# Title  : Zip function in python
# Author : Kiran Raj R.
# Date   : 11:11:2020

languages = ["Malayalam", "tamil", "hindi", "english", "spanish"]
popularity = [10, 20, 50, 100, 40]
area = ['kerala', 'tamil nadu', 'north india', 'world', 'spain']

name =['kiran', 'vishnu', 'manu', 'sivan']
age = [32, 25,24]

first_zip = zip(languages, popularity, area)
second_zip = zip(name, age)

print(first_zip)
print(second_zip)

value1 = list(first_zip)
value2 = set(second_zip)

print(value1)
print(value2)

name ,age = zip(*value2)
print(f"Name: {name} Age: {age} ") 
print("------------------------------------------")
for i in value1:
    print(f"--Language: {i[0]} --Speaks in: {i[1]} --Popularity: {i[2]}")