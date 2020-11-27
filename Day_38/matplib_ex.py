# Title  : Matplotlib
# Author : Kiran Raj R.
# Date   : 21/11/2020

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [4,6,8]
y = [4, 8, 2]

x2 = [3,5,7]
y2 = [9, 1, 3]

plt.plot(x,y,'r',label='first', linewidth=5)
plt.plot(x2,y2,'b',label='second',linewidth=5)

plt.title('First vs Second')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()

plt.grid(True,color='k')

plt.show()