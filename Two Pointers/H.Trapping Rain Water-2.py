class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix = [0] * len(height), [0] * len(height)
        p = s = 0
        res = 0
        for i in range(len(height)):
            prefix[i] = p
            p = max(p, height[i])
        for i in range(len(height) - 1, -1, -1):
            suffix[i] = s
            s = max(s, height[i])
        print(prefix, suffix)
        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            res += water if water > 0 else 0
        return res