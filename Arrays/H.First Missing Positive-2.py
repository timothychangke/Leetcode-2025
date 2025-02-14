class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            idx = abs(nums[i])
            if 0 < idx <= len(nums):
                if nums[idx - 1] == 0:
                    nums[idx - 1] = len(nums) * -1
                elif nums[idx - 1] > 0:
                    nums[idx - 1] = nums[idx - 1] * -1
        print(nums)
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0: return i
        return len(nums) + 1
    
    
    """ 
     def firstMissingPositive(self, nums):
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n
    
    """