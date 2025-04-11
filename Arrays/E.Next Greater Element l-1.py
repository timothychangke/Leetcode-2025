class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = [-1] * len(nums1)
        for i, n in enumerate(nums1):
            d[n] = i
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                x = stack.pop()
                res[d[x]] = n
            if n in d:
                stack.append(n)
        return res

        