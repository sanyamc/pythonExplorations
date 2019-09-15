import os
import sys


def load_words(file):
    " loads the words into an in memory set datastructure and returns it"
    words = set()
    words_list = list()
    try:  
        with open(file, 'r') as f:
            
            for line in f:
                word = line.strip()
                if word not in words:
                    words.add(word)
                    words_list.append(word)
    except IOError as error:
        print("caught exception: "+ error.strerror)

    return words, words_list