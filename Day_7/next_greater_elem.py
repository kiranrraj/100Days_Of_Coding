# Title  : Next Greater Element
# Author : Kiran raj R.
# Date   : 19/07/2025

# Given an array of integers nums, for each element find the next greater element to its right. 
# The next greater element for an element x is the first greater element on the right side of x in the array. 
# If no such element exists, output -1 for that position.

def next_greater(nums):
    n = len(nums)
    res = [-1] * n        # List to store the greatest next number, default to -1
    stack = []            # will store indices

    for i, val in enumerate(nums):
        # resolve any smaller elements waiting in stack
        while stack and val > nums[stack[-1]]:
            idx = stack.pop()
            res[idx] = val
        # now push current index to await its next greater
        stack.append(i)

    return res

if __name__ == "__main__":
    print(next_greater([4, 5, 2, 25]))  

    # Explanation 
    # Step1: i=0, val=4
    #   stack is empty so skip while block, push 0 to stack, stack=[0]
    # Step 2: i=1, val=5
    #   5 > 4 so pop from stack, which is 0, 
    #   add to result list, res[0]=5, now stack, stack=[]
    #   then push i to stack, stack=[1]
    # Step3: i=2, val=2
    #   2 ≤ 5 so skip while block, push 2 to the stack, stack=[1,2]
    # Step4: i=3, val=25:
    #   25 > 2, pop 2 and add to result, res[2]=25, stack become stack=[1]
    #   As the stack is non empty while loop executes, 
    #       25 > 5, pop element 1 and add to result stack, res[1]=25
    #   Add value of i to stack, stack=[3]
    # Step5: Nothing to do as the for loop ends. 
    #   res = [5,25,25,-1]. Index 3 stayed on stack, so res[3] remains -1.


    print(next_greater([13, 7, 6, 12])) 