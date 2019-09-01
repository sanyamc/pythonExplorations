class Solution:
    def __init__(self):
        self.memo=[]

    def canJump_helper(self, A, index):
        if index>= len(A) or index<0:
            return 0
        if index == (len(A) - 1):
            return 1
        if self.memo[index]!= None:
            return self.memo[index]
        max_distance = min(len(A)-1, A[index])

        for i in range(1, max_distance + 1):
            new_index = index + i
            if self.memo[new_index]==1:
                return 1
            val = self.canJump_helper(A, new_index)
            self.memo[new_index] = val
            if val:
                return 1
        self.memo[index] = 0
        return 
        
    def canJump_BU(self, A):
        index = len(A)-2
        self.memo[index+1]=1
        while(index>=0):
            if (len(A)- index -1) <= A[index]:
                self.memo[index] = 1
            else:
                max_dist = min(A[index], len(A)-1)
                for i in range(1, max_dist+1):
                    if self.memo[i+index]==1:
                        self.memo[index]=1
                        break
                if self.memo[index]==None:
                    self.memo[index]=0



            index = index-1
        return self.memo[0]
                
        
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        if len(A) == 0:
            return 0
        self.memo = [None for i in range(len(A))]
        return self.canJump_BU(A)
        return self.canJump_helper(A, 0)

a = [2,3, 1,1,4]
a = [2,3, 1,1,4]
#a=[3,2,1,0,4]
s=Solution()
s.canJump(a)


    