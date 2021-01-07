# Title  : Implement switch
# Author : Kiran Raj R.
# Date   : 29/11/2020

def switch_py(c):
    val_dict  = {
        'one': "Monday",
        'two': 'Tuesday',
        'three':'Wednesday'
    }
    print(val_dict.get(c))
switch_py('one')
switch_py('two')
switch_py('three')