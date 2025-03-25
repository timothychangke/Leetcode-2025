class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        map = {0: 1}
        res = 0
        for n in nums:
            prefix += n
            diff = prefix - k
            res += map.get(diff, 0)
            map[prefix] = map.get(prefix, 0) + 
        return res
    
""" 
1 1 1
p = 0
dict = {0: 1, 1: 1}
"""
