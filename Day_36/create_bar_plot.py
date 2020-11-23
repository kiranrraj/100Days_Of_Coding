# Title  : Bar Graph 
# Author : Kiran Raj R.
# Date   : 19/11/2020

import matplotlib.pyplot as pp

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,10,1,3,5,8,3,10,15,5]

pp.bar(x,y, label="Gold", color="b")
pp.xlabel('Year')
pp.ylabel('Rate')
pp.title("Gold Rate Plot")
pp.legend()
pp.show()
