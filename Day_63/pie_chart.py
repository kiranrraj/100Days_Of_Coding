# Title  : Pie chart
# Author : Kiran Raj R.
# Date   : 19/11/2020

import matplotlib.pyplot as pp

week = [1, 2, 3, 4, 5, 6]
expence = [9, 8, 6, 4, 10, 7]
cols = ['r','y','g','b','m','c']

section = ["Food ", "Recharge", "Electricity", "Water", "Loan", "Petrol"]

pp.pie(week, 
        labels=section, 
        colors = cols, 
        startangle=105, 
        autopct = '%1.2f%%',
        explode=(0,0,0,0,0,0.1)
        )
pp.legend(loc=3)
pp.show()

