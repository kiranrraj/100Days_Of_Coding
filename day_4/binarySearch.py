def b_search(arr, num2find, minPos, maxPos):
    
    mid = (minPos + maxPos) // 2

    if minPos <= maxPos:
        try:
            if arr[mid] == num2find:
                print(f"Element {num2find} found in list {arr} at {mid+1}")
            elif arr[mid] < num2find:
                b_search(arr, num2find, mid+1, maxPos)
            else:
                b_search(arr, num2find, minPos, mid-1)
        except:
            print(f"Element {num2find} not found in list {arr}")
    else:
        print(f"Element {num2find} not found in list {arr}")


list_1 = [23,34,56,78,89,91,101,131,320]
len_list1 = len(list_1)

b_search(list_1, 589, 0, len_list1)