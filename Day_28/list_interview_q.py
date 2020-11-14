# Title  : List interview question.
# Author : Kiran Raj R.
# Date   : 11:11:2020

# Whats the output of the below code ?

# def extendList(val, list=[]):
#     list.append(val)
#     return list

# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
print(list1)                #[10]
list2 = extendList(123,[])
list3 = extendList('a')

print(list1, list2, list3)

#[10, 'a'] [123] [10, 'a']
#Here list1 and list3 got the same output as no seperate list is passed 
#to the function extendedList, both list1 and list2 operate on the same
#default list.

def extendedList_if(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list

list11 = extendedList_if(10)
list21 = extendedList_if(123,[])
list31 = extendedList_if('a')

print(list11, list21, list31)
#[10] [123] ['a']