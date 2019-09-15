'''
    Basic demo of file and strings

'''



'''
 use with context to automatically close the file

'''
def load_file():
    
    words = []
    with open('words.txt','r') as f: # takes care f.close() which is needed by OS
        for line in f:
            word = line.strip("\n")
            words.append(word)
        
    print("Total words {} ".format(len(words)))
    return words


words = load_file()


'''

   strings are as expected immutable

'''

word = words[-1]

print("{} with memory address: {}".format(word, id(word)))
word = word.replace('z','kkkk')
print("{} with memory address: {}".format(word, id(word)))






            