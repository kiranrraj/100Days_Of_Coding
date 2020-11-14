# Title  : Lambda function
# Author : Kiran Raj R.
# Date   : 11:11:2020

#lambda in list 
list_lambda = [lambda x: x**2, lambda y:y**3, lambda x,y: x*y]
print(list_lambda[0](6), list_lambda[1](6), list_lambda[2](2,3))

#lambda in dictionary
dict_lambda = {'2x':lambda x:x**2, '3x':lambda x:x**3}
print(dict_lambda['2x'](10), dict_lambda['3x'](2))

languages = ["Malayalam", "tamil", "hindi", "english", "spanish"]
popularity = [10, 20, 50, 100, 40]
area = ['kerala', 'tamil nadu', 'north india', 'world', 'spain']

name =['kiran', 'vishnu', 'manu', 'sivan']
age = [32, 25,24]

add_num = list(map(lambda x,y:x+y, popularity, age))
print(add_num)
add_string= list(map(lambda x,y:f"{x} : {y}", languages, area))
print(add_string)

print(list(map(lambda x:x.capitalize(), name)))