class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0 , len(nums1) - 1
        while True:
            i = l + (r - l) // 2
            j = (len(nums1) + len(nums2)) // 2 - i - 2
            a1 = nums1[i] if i >= 0 else float('-inf')
            a2 = nums1[i + 1] if i + 1 < len(nums1) else float('inf')
            b1 = nums2[j] if j >= 0 else float('-inf')
            b2 = nums2[j + 1] if j + 1 < len(nums2) else float('inf')
            if b2 >= a1 and a2 >= b1:
                return min(a2, b2) if (len(nums1) + len(nums2)) % 2 else (max(a1, b1) + min(a2, b2)) / 2
            elif a1 > b2:
                r = i - 1
            else:
                l = i + 1