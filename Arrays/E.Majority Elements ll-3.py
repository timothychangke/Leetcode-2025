class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        e1, e2, c1, c2 = 0, 1, 0, 0
        for n in nums:
            if n == e1:
                c1 += 1
            elif n == e2: 
                c2 += 1
            elif c1 == 0:
                e1, c1 = n, 1
            elif c2 == 0:
                e2, c2 = n, 1
            else:
                c1 -= 1
                c2 -= 1
        return [e for e in (e1, e2) if nums.count(e) > len(nums) // 3]
    
        
sol = Solution()
print(sol.majorityElement([0,0,0,0]))
    
            