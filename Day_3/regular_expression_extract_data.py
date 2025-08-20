# Author    : Kiran raj R.
# Date      : 20/08/2025
# Question  : Regular Expression - Extracting and Storing Data in a Dictionary
#----------------------------------------------------------

import re

log_entries = [
    "ERROR: User 101 failed login at 2023-10-26.",
    "INFO: User 205 logged in successfully at 2023-10-26.",
    "WARNING: Inactive user 302 access attempt."
]

log_pattern = r"^(ERROR|INFO|WARNING): User (\d+)"

parsed_logs = {}

for entry in log_entries:
    match = re.search(log_pattern, entry)
    if match:
        print(match.group())
        # Group 1 is the log level (ERROR, INFO, WARNING)
        log_level = match.group(1)  
        # Group 2 is the user ID
        user_id = match.group(2)    
        
        # Store the user ID under its log level
        if log_level not in parsed_logs:
            parsed_logs[log_level] = []
        parsed_logs[log_level].append(user_id)

print(parsed_logs)
# Output: {'ERROR': ['101'], 'INFO': ['205'], 'WARNING': ['302']}