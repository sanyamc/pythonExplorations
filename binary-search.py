class Solution:
    
    def b_search(self, nums, start, end, B):
        
        while(start <= end):
            mid = (start + end)//2
            if nums[mid] == B:
                return mid
            elif nums[mid]>B:
                end = mid -1
            else:
                start = mid +1
        return -1
    
    def find_pivot(self, A):
        incr = True
        pivot = -1
        
        for i in range(1, len(A)):
            if A[i]>A[i-1]:
                continue
            else:
                pivot = i
                
                break
        if pivot == -1:
            return -1
        
        if pivot<len(A):
            for i in range(pivot+1, len(A)):
                if A[i]>A[i-1]:
                    continue
                else:
                    incr = False
                    break
        
        if incr==True:
            return pivot
        else:
            for i in range(1, len(A)):
                if A[i]<A[i-1]:
                    continue
                else:
                    return i
            
        
                
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        if len(A) ==0:
            return -1
        if len(A)==1:
            if A[0]==B:
                return 0
            else:
                return -1
                
        start = 0
        end = len(A) - 1
        while( start <= end):
            mid = (start + end)//2
            if A[mid] == B:
                return mid
            if A[start] < A[mid]:
                if A[start]<=B<=A[mid]:
                    return self.b_search(A, start, mid, B)
            if A[mid+1] < A[end]:
                if A[mid+1]<=B<=A[end]:
                    return self.b_search(A, mid+1, end, B)
            if A[start] > A[mid] and (A[start] >= B >=A[mid]):
                end = mid
            if A[mid+1] > A[end] and (A[mid+1] >=B >=A[end]):
                start = mid+1
        
        return -1
            
                



s=Solution()
nums =  [ 19, 20, 21, 22, 28, 29, 32, 36, 39, 40, 41, 42, 43, 45, 48, 49, 51, 54, 55, 56, 58, 60, 61, 62, 65, 67, 69, 71, 72, 74, 75, 78, 81, 84, 85, 87, 89, 92, 94, 95, 96, 97, 98, 99, 100, 105, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 130, 131, 133, 134, 135, 136, 137, 138, 139, 141, 142, 144, 146, 147, 148, 149, 150, 153, 155, 157, 159, 161, 163, 164, 169, 170, 175, 176, 179, 180, 185, 187, 188, 189, 192, 196, 199, 201, 203, 205, 3, 7, 9, 10, 12, 13, 17 ]
B = 6
val = s.search(nums,B)
print(val)