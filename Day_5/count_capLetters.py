# Author    : Kiran raj R.
# Date      : 22/08/2025
# Question  : Count capital letters in a sentence


text1 = """Web sites are written using HTML, which means that each web page is a structured document. 
Sometimes it would be great to obtain some data from them and preserve the structure while we’re at it. 
Web sites don’t always provide their data in comfortable formats such as CSV or JSON. This is where web 
scraping comes in. Web scraping is the practice of using a computer program to sift through a web page 
and gather the data that you need in a format most useful to you while at the same time preserving the 
structure of the data."""

def countCapital(text1):
    capital = 0
    for char in text1:
        if char.isupper():
            capital+=1
    return capital

print(f"Number of capitals in the text is {countCapital(text1)}")