# Author    : Kiran raj R.
# Date      : 20/08/2025
# Question  : Regular Expression - Email check
#----------------------------------------------------------

import re

def is_valid_email(email):
    # A common regex pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

# --- Test Cases ---
print("--- Testing valid email addresses ---")
print(f"test@example.com is valid: {is_valid_email('test@example.com')}")
print(f"user.name+tag@domain.co.in is valid: {is_valid_email('user.name+tag@domain.co.in')}")
print(f"12345@sub.domain.net is valid: {is_valid_email('12345@sub.domain.net')}")

print("\n--- Testing invalid email addresses ---")
print(f"invalid-email is valid: {is_valid_email('invalid-email')}")
print(f"no@domain is valid: {is_valid_email('no@domain')}")
print(f"@domain.com is valid: {is_valid_email('@domain.com')}")
print(f"user@.com is valid: {is_valid_email('user@.com')}")


### 1.Username Part: ^[a-zA-Z0-9._%+-]+
# ^: Anchors the pattern to the beginning of the string. This ensures the 
# match starts from the first character.
# [a-zA-Z0-9._%+-]: This is a character set that defines the allowed 
# characters for the username. 
# +: This quantifier means the preceding character set must appear one 
# or more times. It ensures the username isn't empty.

### 2. The @ Symbol: @
# @: Matches the literal "at" symbol. This separates the username from 
# the domain.

### 3. Domain Part: [a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
# [a-zA-Z0-9.-]+: This character set matches one or more characters for 
# the domain name itself. It allows letters, numbers, dots, and hyphens.
# \.: Matches a literal dot (.). The backslash \ is an escape character
# that tells the regex engine to treat the dot as a literal character, 
# not the wildcard metacharacter. This dot separates the domain from 
# the top-level domain.
# [a-zA-Z]{2,}: This part matches the top-level domain like com or org. 
# {2,}: This quantifier specifies that the preceding character set must
# appear at least two times.
# $: Anchors the pattern to the end of the string. 