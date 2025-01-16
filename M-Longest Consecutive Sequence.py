class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) 
        explored = set()
        res = 0 
        for n in nums:
            if n not in explored and n - 1 not in num_set:
                c = 0
                while n + c in num_set:
                    c += 1
                res = max(res, c) 
            explored.add(n)      
        return res
        
""" 
need to be in O(n)
create a hash set with the key as the value and the value as the index
for each element, see if the ele - 1 is in the set
loop until that element is not in the set
this shall be the starting point
loop until the end is reached
record this as the length
repeat until all visited

add an explored set so as to not waste time visiting them again as they are not the ends of the sequence we are looking for
"""