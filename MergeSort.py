in_count = 0


class Solution:

    def __init__(self):
        self.in_count = 0
        self.small_array =[]

    def merge_sort(self,nums, start, end):
        global in_count

        if start == end:
            return

        mid = (start + end) // 2
        left = []
        right = []
        self.merge_sort(nums, start, mid)
        self.merge_sort(nums, mid + 1, end)
        result = []

        left_limit = start
        right_limit = mid + 1
        temp = 0
        while(left_limit <= mid or right_limit <= end):
            if (left_limit <= mid and right_limit <= end):
                if (nums[left_limit] <= nums[right_limit]):
                    result.append(nums[left_limit])
                    self.small_array[left_limit] += temp
                    left_limit += 1
                elif nums[right_limit] < nums[left_limit]:
                    #self.in_count += 1
                    temp +=1
                    result.append(nums[right_limit])
                    right_limit += 1
            elif left_limit <= mid:
                result.append(nums[left_limit])
                self.small_array[left_limit] += temp
                #self.in_count += 1
                left_limit += 1
            else:
                #temp = 0
                result.append(nums[right_limit])
                #in_count += 1
                right_limit += 1

        i = start
        k = 0
        while(i <= end):
            nums[i] = result[k]
            i += 1
            k += 1


#nums = [3, 1, 5, 6, 4]
nums = [5, 3, 2, 4, 4, 35, 1, 14, 38, 35, 2]

def countSmallerToTheRight(nums):
    s=Solution()
    s.small_array = [0 for i in nums]
    s.merge_sort(nums,0,len(nums)-1)
    return s.small_array

v = countSmallerToTheRight(nums)


print("small array {} ".format(v))
