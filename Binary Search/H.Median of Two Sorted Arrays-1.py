class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = (len(nums1) + len(nums2)) // 2 - i - 2
            a1, a2, b1, b2 = nums1[i] if i >= 0 else float('-inf'), nums1[i + 1] if i + 1 < len(nums1) else float('inf'), nums2[j] if j >= 0 else float('-inf'), nums2[j + 1] if j + 1 < len(nums2) else float('inf')
            if a1 <= b2 and b1 <= a2:
                if (len(nums1) + len(nums2)) % 2:
                    return min(a2, b2)
                else:
                    return (max(a1, b1) + min(a2, b2)) / 2
            elif b2 < a1:
                r = i - 1
            else:
                l = i + 1
