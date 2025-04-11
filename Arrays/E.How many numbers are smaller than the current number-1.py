class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = [0] * 101
        for num in nums: n[num] += 1
        prefix = 0
        for i in range(len(n)):
            temp = n[i]
            n[i] = prefix
            prefix += temp
        return [n[i] for i in nums]