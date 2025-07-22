# Title  : Simulates a customer service queue to determine service order and total time.
# Author : Kiran raj R.
# Date   : 22/07/2025


from collections import deque

def customer_service_queue(service_times: list[int]) -> tuple[list[int], int]:
    
    # Initialize the queue
    customer_queue = deque()

    served_order = []
    total_service_time = 0
    
    # Enqueue customers as they arrive
    for time in service_times:
        # Add to the right (end of the queue)
        customer_queue.append(time) 
        
    # Dequeue and process customers
    while customer_queue:
        # Remove from the left (front of the queue)
        current_customer_time = customer_queue.popleft() 
        
        served_order.append(current_customer_time)
        total_service_time += current_customer_time
        
    return served_order, total_service_time

print("--- Test Case 1 ---")
service_times_1 = [5, 2, 8, 3]
order_1, total_time_1 = customer_service_queue(service_times_1)
print(f"Input: {service_times_1}")
print(f"Served Order: {order_1}")
print(f"Total Service Time: {total_time_1}")


print("\n--- Test Case 2 ---")
service_times_2 = [10, 1, 4]
order_2, total_time_2 = customer_service_queue(service_times_2)
print(f"Input: {service_times_2}")
print(f"Served Order: {order_2}")
print(f"Total Service Time: {total_time_2}")
