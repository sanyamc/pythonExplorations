
max_index = (0,0)
max_length = 0
def helper(str1, str2):
    global max_length
    if len(str1)==0 or len(str2)==0:
        return max(len(str1), len(str2))
        # if len(so_far) > max_length:
        #     max_length = len(so_far)
            
            #max_index = so_far[0],so_far[-1]
        #print(so_far)
        #so_far=[]
        #return
    if str1[0] == str2[0]:
        #so_far.append(str1[0])    
        return helper(str1[1:], str2[1:])
        #so_far.pop()
    else:
        val = min( helper(str1[1:], str2)+1,
        helper(str1,str2[1:])+1,
        helper(str1[1:], str2[1:])+1) # this one is interesting
        return val

def helper_fast(str1, str2):
    



#helper("received", "ere", [])

# TODO:
# change it to produce index in smaller array
# write recursive equation


        
