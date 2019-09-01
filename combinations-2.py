def helper(nums, used, k, index, curr_size):
    if curr_size == k:
        [print(nums[i], end="") for i in range(len(nums)) if used[i]==True]
        print("")
        return
    
    if index == len(nums):
        return

    used[index] = True
    helper(nums, used, k, index+1, curr_size+1)
    used[index] = False
    helper(nums, used, k, index+1, curr_size)

def combine(nums,k):
    if k>=len(nums):
        return
    used = [False for i in nums]
    helper(nums, used, k, 0, 0)

nums = [1,2,3,4]
combine(nums, 2)
print("done")
combine(nums, 3)

