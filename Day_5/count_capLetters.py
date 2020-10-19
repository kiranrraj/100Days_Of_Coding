# Title  : Count capital letters in a sentence
# Author : Kiran raj R.
# Date   : 19:10:2020

capital = 0

text = """Web sites are written using HTML, which means that each web page is a structured document. 
Sometimes it would be great to obtain some data from them and preserve the structure while we’re at it. 
Web sites don’t always provide their data in comfortable formats such as CSV or JSON. This is where web 
scraping comes in. Web scraping is the practice of using a computer program to sift through a web page 
and gather the data that you need in a format most useful to you while at the same time preserving the 
structure of the data."""

for char in text:
    if char.isupper():
        capital+=1

print(capital)