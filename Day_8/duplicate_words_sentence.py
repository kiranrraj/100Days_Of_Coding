# Title  : Remove duplicate words from sentence
# Author : Kiran raj R.
# Date   : 22:10:2020

userInput = input('Enter a sentence to remove duplicate words : ')
word_list = userInput.lower().strip().split()



def removeDupwords(sentence):
    new_list = []

    for i in range(len(sentence)):
        for j in range(i+1):
            if sentence[i] == sentence[j]:
                break
        if i == j:
            new_list.append(sentence[i])
  
    return (" ".join(new_list))


print('-'*25)
print(removeDupwords(word_list))

