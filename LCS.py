
memo=[]

def LCS(str1, str2):
    if len(str1)==0 or len(str2)==0:
        return ""
    else:
        return LCS_helper(str1, str2,[])

def LCS_helper(str1, str2, so_far):
    if len(str1)==0 or len(str2)==0:
        return so_far
    
    if str1[0] == str2[0]:
        so_far.append(str1[0])
        return LCS_helper(str1[1:],str2[1:], so_far.copy())
    else:
        val1 = LCS_helper(str1[1:], str2, so_far.copy())
        val2 = LCS_helper(str1, str2[1:], so_far.copy())
        val3 = LCS_helper(str1[1:], str2[1:], so_far.copy())
        max_len = max(len(val1), len(val2), len(val3))
        if len(val1) == max_len:
            return val1
        elif len(val2) == max_len:
            return val2

def LCS_fast(str1, str2):
    global memo
    if len(str1)==0 or len(str2)==0:
        return ""
    else:
        memo=[[None for i in range(len(str2))] for j in range(len(str1))]
        #print(memo)
        return LCS_memo(str1, str2,[])
    

def LCS_memo(str1, str2, so_far):
    global memo
    if len(str1)==0 or len(str2)==0:
        #print("memo {}".format(memo))
        return so_far
    i = len(str1)-1
    j = len(str2)-1
    #print("i:{}, j:{}".format(i,j))
    if memo[i][j] != None:
        print("memo {}".format(memo))
        return memo[i][j].copy()
    
    if str1[0] == str2[0]:
        so_far.append(str1[0])
        val = LCS_memo(str1[1:],str2[1:], so_far.copy())
        print("val is: {}".format(val))
        memo[i-1][j-1] = val.copy()
        return val
    else:
        val1 = LCS_memo(str1[1:], str2, so_far.copy())
        memo[i-1][j]=val1.copy()
        val2 = LCS_memo(str1, str2[1:], so_far.copy())
        memo[i][j-1]=val2.copy()
        #val3 = LCS_helper(str1[1:], str2[1:], so_far.copy())
        max_len = max(len(val1), len(val2))
        if len(val1) == max_len:
            #memo[i][j] = val1.copy()

            return val1
        elif len(val2) == max_len:
            #memo[i][j] = val2.copy()
            return val2
