class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        k = 0
        for n in nums:
            if n not in s:
                s.add(n)
                nums[k] = n
                k += 1
        return k
            

        