
'''
class Solution:
    def __init__(self):
        self.result=[]

    def fast_helper(self, k,n, so_far):
        if len(so_far)>k:
            return

        if len(so_far)==k:
            self.result.append(so_far+[])
            return
        # if n>k:
        #     return       
        
        #val = inputSet.pop(0)


        self.fast_helper(k, n+1,so_far+[])
        so_far.append(n+1)
        self.fast_helper(k, n+1, so_far+[])
    
    def helper(self, k, inputSet, so_far):
        if len(so_far)>k:
            return

        if len(so_far)==k:
            self.result.append(so_far+[])
            return
        if len(inputSet)==0:
            return       
        
        val = inputSet.pop(0)


        self.helper(k,inputSet+[],so_far+[])
        so_far.append(val)
        self.helper(k, inputSet+[], so_far+[])
        #so_far.pop()

        #inputSet.append(val)
        
        
        
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):
        if k>n:
            return
            
        inputSet=[i for i in range(1, n+1)]
        self.result=[]
        if k==n:
            return inputSet
        self.fast_helper(k,1,[])
        #self.helper(k,inputSet,[])
        return self.result[::-1]
'''

class Solution:
    def __init__(self):
        self.result=[]
    
    def rec_helper(self, A, target, so_far, so_far_sum):
        if so_far_sum > target:
            return
        if so_far_sum == target:
            s = sorted(so_far)
            if s not in self.result:
                self.result.append(s)
            #self.result.add(sorted(so_far))
            return
        if len(A)==0:
            return
        val = A.pop()
        self.rec_helper(A+[], target, so_far+[], so_far_sum)
        self.rec_helper(A+[], target, so_far+[val], so_far_sum+val)
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        if len(A)==0:
            return A
        if B<0:
            return []
        self.result = []
        self.rec_helper(A,B,[],0)
        
        #print(self.result)
        return self.result


s=Solution()
s.combinationSum([10,1,2,7,6,1,5],8)
