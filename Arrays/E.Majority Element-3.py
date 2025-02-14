class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele, c = '', 0
        for n in nums:
            if c == 0: 
                ele = n
                c += 1
            else:
                if ele == n: c += 1
                else: c -= 1
        return ele

        