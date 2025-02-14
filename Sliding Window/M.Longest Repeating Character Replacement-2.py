class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0] * 26
        maxCount, l = 0, 0
        for r in range(len(s)):
            arr[ord(s[r]) - ord('A')] += 1
            maxCount = max(arr[ord(s[r]) - ord('A')], maxCount)
            if r - l + 1 - maxCount > k:
                arr[ord(s[l]) - ord('A')] -= 1
                l += 1
        return len(s) - l
            
                