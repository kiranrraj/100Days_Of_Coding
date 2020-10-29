# Title  : Find largest and smallest words in a string
# Author : Kiran raj R.
# Date   : 21:10:2020

def smallest_largest_word(words):

    words_list = words.split()
    smallest_word = words_list[0]
    largest_word = words_list[0]

    for word in words_list:
        if len(smallest_word) > len(word):
            smallest_word = word

        if len(largest_word) < len(word):
            largest_word = word

    print(f"The string user provided is: {words}")
    print(
        f"The largest word is: {largest_word}\nThe smallest word is: {smallest_word}")


smallest_largest_word("hello worl23d my note over")
