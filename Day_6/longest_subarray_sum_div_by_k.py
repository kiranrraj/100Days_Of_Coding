# Title  : Longest Subarray with Sum Divisible by K
# Author : Kiran raj R.
# Date   : 18/07/2025

# remainder 0 “seen” before the array begins
first_index = { 0: -1 }    
prefix = 0
max_len = 0

for i, x in enumerate(arr):
    # Update running sum modulo K
    prefix = (prefix + x) % K

    # Normalize negative prefix
    if prefix < 0:
        prefix += K

    # If we’ve seen this remainder before, a valid subarray exists
    if prefix in first_index:
        # the subarray (first_index[prefix]+1 ... i) sums to multiple of K
        curr_len = i - first_index[prefix]
        max_len = max(max_len, curr_len)
    else:
        # Otherwise, record this as the first occurrence of this remainder
        first_index[prefix] = i

return max_len
