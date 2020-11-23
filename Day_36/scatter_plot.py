# Title  : Pie chart
# Author : Kiran Raj R.
# Date   : 19/11/2020

import matplotlib.pyplot as pp

x = [1,2,3,4,5]
y = [5,10,5,10,15]

pp.scatter(x,y, color='b', label="Gold Price")

pp.xlabel('X-axis')
pp.ylabel('Y-axis')
pp.title('Scatter Plot')
pp.legend()
pp.show()