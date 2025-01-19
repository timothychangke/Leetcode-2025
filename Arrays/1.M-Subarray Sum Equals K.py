class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0:1}
        prefix = 0
        res = 0
        for i in range(len(nums)):
            prefix += nums[i]
            diff = prefix - k
            res += map.get(diff, 0)
            map[prefix] = map.get(prefix, 0) + 1
        return res
""" 
create a prefix sum
two pointers? sliding window?
create a map containing the occurances of prefixsums
iterate thru the list and add the prefixes into the map
if there exist k - prefix in the map as well, this means that prefix - (prefix - k) = k and res can increment by the number of occurances of k - prefix

TC: O(n) SC: O(n)

"""
