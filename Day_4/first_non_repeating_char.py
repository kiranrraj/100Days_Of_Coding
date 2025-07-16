# Title  : Find first non repeating char
# Author : Kiran raj R.
# Date   : 16/07/2025

def first_non_repeating_char_ignore_case(s: str) -> str | None:
    # Count frequencies ignoring case
    char_count = {}
    for ch in s:
        ch_lower = ch.lower()
        char_count[ch_lower] = char_count.get(ch_lower, 0) + 1

    for ch in s:
        if char_count[ch.lower()] == 1:
            return ch

    return None


# Test cases
print(first_non_repeating_char_ignore_case("swiss"))    
print(first_non_repeating_char_ignore_case("aabbcc"))      
print(first_non_repeating_char_ignore_case("x"))        
print(first_non_repeating_char_ignore_case("AaBbCc"))       
print(first_non_repeating_char_ignore_case("a b c a b"))    
print(first_non_repeating_char_ignore_case(""))             