from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        c1, c2, n1, n2 = 0, 0, 0, 1
        for n in nums:
            if n == n1:
                c1 += 1
            elif n == n2: 
                c2 += 1
            elif c1 == 0:
                n1, c1 = n, 1
            elif c2 == 0:
                n2, c2 = n, 1
            else:
                c1 -= 1
                c2 -= 1
        return [n for n in (n1, n2) if nums.count(n) > len(nums) // 3]