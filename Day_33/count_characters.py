# Title  : Find the number of characters
# Author : Kiran Raj R.
# Date   : 16/11/2020

dict_ch = {}

with open('words.txt') as file:
    for line in file:
        line = line.strip()
        for ch in line:
            if ch in dict_ch.keys():
                dict_ch[ch]+=1
            else:
                dict_ch[ch] = 1

    print(f"Characters in 'words.txt' is:")
    for i in dict_ch:
        print(f"{i} --- {dict_ch[i]}")

    # for k,v in dict_ch.items():
    #     print(f"{k} --- {v}")