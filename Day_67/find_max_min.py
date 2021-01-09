# Title  : Find the min and max element in a array
# Author : Kiran raj R.
# Date   : 

def getMin(arr, n): 
    res = arr[0] 
    for i in range(1, n, 1): 
        res = min(res, arr[i]) 
    return res 
 
def getMax(arr, n): 
    res = arr[0] 
    for i in range(1, n, 1): 
        res = max(res, arr[i]) 
    return res