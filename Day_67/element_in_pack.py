# Title  : In the array of n find specified element in a block of k elements 
# Author : Kiran raj R.
# Date   : 

def findxinkindowSize(arr, x, k, n) : 
  
    i = 0
    while i < n : 
  
        j = 0
          
        while j < k : 
              
            if arr[i + j] == x : 
                break
              
            j += 1
  
        if j == k : 
            return False
  
        i += k 
   
    if i == n : 
        return True
  
    j = i - k 

    while j < n : 
        if arr[j] == x : 
            break
  
        j += 1
  
    if j == n : 
        return False
  
    return True