# Title  : Bar Graph With 2 Graph
# Author : Kiran Raj R.
# Date   : 19/11/2020

import matplotlib.pyplot as pp

x1 = [1,3,5,7,9]
y1 = [10,4,8,3,9]

x2 = [2,4,6,8,10]
y2 = [5,10,5,7,11]

pp.bar(x1,y1, label="Gold", color="b")
pp.bar(x2,y2, label="Silver", color="r")
pp.xlabel('Month')
pp.ylabel('Rate')
pp.title("Gold Rate Plot")
pp.legend()
pp.show()
