# Author    : Kiran raj R.
# Date      : 22/08/2025
# Question  : Valid Amstrong


def validAmstrong(num):
    original_num = num

    if num >= 0 and num <= 9:
        return True

    power = len(str(num))
    total_sum = 0
    temp_num = num
    
    while temp_num > 0:
        digit = temp_num % 10
        total_sum += digit ** power
        temp_num //= 10
        
    return total_sum == original_num

# Test
for i in [1, 2, 3, 4, 5, 100, 120, 153, 300, 370, 371, 400, 407]:
    print(f"Is {i} a valid Armstrong? {validArmstrong(i)}")


# Time complexity:  O(log10 n)
# Space complexity: O(1)