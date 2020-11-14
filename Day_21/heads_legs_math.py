# Title  : Heads and legs math problem
# Author : Kiran Raj R.
# Date   : 04:11:2020

heads = 35
legs = 94

#calculating how many chickens and goats
#assume i rep cu=hicken and j rep goats
def find_number(heads, legs):
    num = {'i':[], 'j':[]}
    for i in range(heads+1):
        j=heads - i # heads must be equal to i+j
        # print(i,j)
        if i*2 + j *4 == legs:
            num['i'].append(i)
            num['j'].append(j)
            # return f"We have {i} chickens and {j} goats"
    if num['i']==[] and num['j']==[] :
        print("No solution found")
    else:
        for k in range(len(num['i'])):
            return print(f"We have {num['i'][k]} chickens and {num['j'][k]} goats")

print(find_number(heads, legs))