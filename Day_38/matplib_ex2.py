from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('value.csv',
                 unpack=True,
                 delimiter = ',')

plt.plot(x,y)

plt.title('Value from file')
plt.ylabel('Amp')
plt.xlabel('Scale')

plt.show()