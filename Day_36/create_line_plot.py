# Title  : Line graph
# Author : Kiran Raj R.
# Date   : 19/11/2020

import matplotlib.pyplot as pp

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,10,1,3,5,8,3,10,15,5]

pp.plot(x,y, label="Line Plot", color="r")
pp.xlabel('Year')
pp.ylabel('Rate')
pp.title("Rate Plot")
pp.legend()
pp.show()

