# Title  : Regular Expression
# Author : Kiran Raj R.
# Date   : 28/11/2020


import re 
  
fn = ["index.html", "data.xml",  
            "serial.txt", "dog.jpg"] 
  
for file in fn:  
    out= re.search("\.xml$", file) 
  
    if out: 
        print(f"The filename of file with extension .xml is: {file}")