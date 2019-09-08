import load_dictionary
import palindromes
import time


def get_palingrames(words_list=None, words_set=None):
    
    '''
        Idea is to create 2 slices of word and see if initial part is present in dictionary in reverse form.
        for e.g. nurses could be combined with "nurses run" which is a palingram

        here is my algorithm for splitting the string

            - go through each word
            - if word length is even go one extra else goto half of length
            - use splice of string using word[i::-1] which gets the first part from nurses in reverse order like run and
            - use splice to get remaining word and see if its a palindrome if yes then add the word found in first and add it to palingram

    '''
    
    if words_list==None:
        words_set, words_list = load_dictionary.load_words("C:\\github\\pythonExplorations\\Palingrams\\words.txt")

    palingrames = list()

    for word in words_list:
        limit = int(len(word))
        for i in range(0, limit):
            first_word = word[i::-1]
            second_word = word[(i+1)::]
            if first_word in words_set and palindromes.is_palindorm(second_word):
                palingrames.append(word+ " "+ first_word)

            if second_word[::-1] in words_set and palindromes.is_palindorm(first_word):
                palingrames.append(second_word[::-1]+ " "+ word)

    print("Palingrames found in file were: {}".format(len(palingrames)))
    return palingrames


start = time.time()
get_palingrames()
end = time.time()
print("total time took was {} seconds".format((end-start)))
