class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window: return True
            window.add(nums[r])
        return False
""" 
k is the maximum size of the window
have a left and right pointer. make it expand and shrink based on the maximum size of k
"""