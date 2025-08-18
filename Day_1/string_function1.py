# Author    : Kiran raj R.
# Date      : 18/08/2025
# Question  : String functions
# --------------------------------------------------------------------------
# Immutable : once created, can’t be changed (operations create new strings).
# Ordered   : indexing & slicing works.
# Iterable  : you can loop through characters.
# Quotes    : Can be enclosed in "double", 'single', or """triple quotes"""
# --------------------------------------------------------------------------


# Find length of string
string1 = "Hello World"
print("# Find length of string")
print(f"Length of {string1} is: {len(string1)}")


# Indexing
print("\n### Indexing ###")
print(f"First char of {string1} is: {string1[0]}")
print(f"Last char of {string1} is: {string1[-1]}")
print(f"Middle chars of {string1} is: {string1[1:-1]}")
print(f"Reverse {string1}: {string1[::-1]}")
print(f"Alternate words of {string1}: {string1[::2]}")


# Case Conversion
print("\n### Case Conversion ###")
string1 = "hai hello"
string2 = "HELLO"
string3 = "This is Excellent"
print(f"{string1}.upper() => {string1.upper()}")
print(f"{string2}.lower() => {string2.lower()}")
print(f"{string1}.title() => {string1.title()}")
print(f"{string1}.capitalize() => {string1.capitalize()}")
print(f"{string3}.swapcase() => {string3.swapcase()}")


# Search
print("\n### Search ###")
string4 = "Hello World"
print(f'({string4}).find("o") [First index of "o"] => {string4.find("o")}')
print(f'({string4}).rfind("o") [Last index of "o"] => {string4.rfind("o")}')
print(f"{string4}.count('o') [Count occurrences] => {string4.count('o')}")
try:
    print(f'({string4}).index("x") [find index of "x", if not found error] => {string4.index("x")}')
except:
    print(f"Error while checking.")


# Validation
print("\n### Validation ###")
print(f'"123".isdigit()     =>  {"123".isdigit()}')
print(f'"World".isdigit()   =>  {"World".isdigit()}')
print(f'"abc".isalpha()     =>  {"abc".isalpha()}')
print(f'"123".isalpha()     =>  {"123".isalpha()}')
print(f'"abc123".isalnum()  =>  {"abc123".isalnum()}')
print(f'"123".isalnum()     =>  {"123".isalnum()}')
print(f'"abc".isalnum()     =>  {"abc".isalnum()}')
print(f'"   ".isspace()     =>  {"   ".isspace()}')
print(f'"  HO  ".isspace()  =>  {"  HO  ".isspace()}')
print(f'"Hello".istitle()   =>  {"Hello".istitle()}')
print(f'"hello".istitle()   =>  {"hello".istitle()}')
print(f'"hello".islower()   =>  {"hello".islower()}')
print(f'"heLLo".islower()   =>  {"heLLo".islower()}')
print(f'"HELLO".isupper()   =>  {"HELLO".isupper()}')
print(f'"HEllo".isupper()   =>  {"HEllo".isupper()}')


# Stripping 
print("\n### Stripping ###")
print(f'"  hello  ".strip() => "{"  hello  ".strip()}"')
print(f'"  hello  ".lstrip() => "{"  hello  ".lstrip()}"')
print(f'"  hello  ".rstrip() => "{"  hello  ".rstrip()}"')


# Replace 
print("\n### Replace ###")
print(f'"hello world".replace("world", "Python") => {"hello world".replace("world", "Python")}')


# zfill
print("\n### zfill ###")
print(f"'423'.zfill(10) => {'423'.zfill(10)}")
print(f"'abc'.zfill(10) => {'abc'.zfill(10)}")


# startswith & endswidth
print("\n### startswith & endswidth ###")
print(f"'Hello'.startswith('He')  => {'Hello'.startswith('He')}")
print(f"'Hello'.startswith('Hee') => {'Hello'.startswith('Hee')}")
print(f"'Hello'.endswith('lo')    => {'Hello'.endswith('lo')}")
print(f"'Hello'.endswith('loo')   => {'Hello'.endswith('loo')}")