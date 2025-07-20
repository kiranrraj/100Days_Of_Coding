# Title  : Daily temperature
# Author : Kiran raj R.
# Date   : 20/07/2025

# Given a list of daily temperatures, return a list such that, for each day in the input, tells you how many days 
# you would have to wait until a warmer temperature. If there is no future day for which this is possible, keep 0 instead.

# This solution uses a monotonic decreasing stack. The stack stores the indices of the temperatures.

# We iterate through the temperatures. For each temperature, we check the top of the stack. If the current temperature 
# is warmer than the temperature at the index on top of the stack, it means we've found a warmer day for that previous day.
# We pop the index from the stack, calculate the number of days waited (current index - popped index), and update our result 
# list. We repeat this until the stack is empty or the current temperature is no longer warmer than the one at the top.

# Finally, we push the current day's index onto the stack, maintaining the monotonic (decreasing) order.


from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    # Initialize the result list with all zeros. The size is the same as the input.
    # Any day that remains 0 means no warmer future day was found.
    result = [0] * len(temperatures)
    
    # The stack will store indices of the temperatures.
    stack = []

    # Enumerate through the temperatures to get both index and value.
    for i, temp in enumerate(temperatures):
        # While the stack is not empty AND the current temperature is warmer
        # than the temperature at the index stored at the top of the stack...
        while stack and temp > temperatures[stack[-1]]:
            # Pop the index of the previous, cooler day.
            prev_index = stack.pop()
            # Calculate the difference in days and update the result.
            result[prev_index] = i - prev_index
        
        # Push the current day's index onto the stack.
        stack.append(i)
        
    return result

temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
print(f"Temperatures: {temps1}")
print(f"Days to wait: {daily_temperatures(temps1)}") 

temps2 = [30, 40, 50, 60]
print(f"\nTemperatures: {temps2}")
print(f"Days to wait: {daily_temperatures(temps2)}") 