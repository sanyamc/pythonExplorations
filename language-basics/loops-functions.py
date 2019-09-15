

def get_index():
    ''''
    shows how to get index and value in a for loop
    '''

    for index, val in enumerate("samplestring"):
        print('index: {}, value: {}'.format(index,val))



'''
    sorting

'''
def display_sorting(input, key):
    input.sort(key=key)
    for val in input:
        print(val)


input = [{'name':'bb', 'val':12}, {'name':'a','val':9}]





if __name__ == "__main__":
    get_index()
    display_sorting(input, lambda val: val['name'])





