import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        if len(self.nums) >= self.k:
            heapq.heappushpop(self.nums, val)
        else: heapq.heappush(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)