class Solution:
    def __init__(self):
        self.result = []
        self.flag =False
    
    def helper(self, so_far, A):
        if len(so_far)==pow(2, A):
            self.result=[int(i,2) for i in so_far]
            return
        rev = so_far[::-1]
        new_s=[]
        for i in so_far:
            new_s.append('0'+i)
        for i in rev:
            new_s.append('1'+i)
        self.helper(new_s, A)
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):

        so_far=['']
        self.helper(so_far,A)



        return self.result



    def generate(self, val):
        result=[]
        for i in range(len(val)):
            if val[i]=='0':
                temp = val[:i]+'1'+val[(i+1):]
                result.append(temp)
        return result.copy()


    def helperBFS(self, so_far, A):
        candidates = []
        candidates.append(so_far)
        while(len(candidates)>0):
            val = candidates.pop(0)
            if int(val,2) not in self.result:
                self.result.append(int(val,2))
            temp = self.generate(val)
            for i in temp:
                if i not in candidates:
                    candidates.append(i)
            #candidates = candidates + self.generate(val)
        
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):

        so_far=['']
        self.helper(so_far,A)



        return self.result

s=Solution()
s.grayCode(3)