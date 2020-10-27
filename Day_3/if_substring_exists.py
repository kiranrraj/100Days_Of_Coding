# Title  : If all elements of substring is in the sentence
# Author : Kiran raj R.
# Date   : 17:10:2020

list1 = ["kiran raj r", "kiran raj", "kiran r"]
sub = ["raj", "r"]

list2 = ["python is good", "javascript is also good", " python programming"]
sub2 = ["is", "good"]
sub3 = ["python", "is"]


def substring_needed(list_in, subs_list):
    found = True
    out_list = []
    for sentence in list_in:
        for elem in subs_list:
            # print(sentence, elem)
            if elem not in sentence:
                found = False
                break
        if found == True:
            out_list.append(sentence)
    print(out_list)


substring_needed(list1, sub)
substring_needed(list2, sub2)
substring_needed(list2, sub3)
