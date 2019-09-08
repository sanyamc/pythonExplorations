import load_dictionary


def get_palindromes(words_list):
    palindromes = list()

    for word in words_list:
        if is_palindrom(word):
            palindromes.append(word)

    return palindromes

def is_palindorm(word):
    start = 0
    end = len(word)-1
    while start<=end:
        if word[start] == word[end]:
            start+=1
            end-=1
        else:
                break
    if start>end:
        return True




'''
s,l = load_dictionary.load_words("words.txt")
get_palindromes(l)

'''
