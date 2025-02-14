class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = start = 0
        a = [0] * 26
        for end in range(len(s)):
            a[ord(s[end]) - ord('A')] += 1
            maxCount = max(maxCount, a[ord(s[end]) - ord('A')])
            if end - start + 1 - maxCount > k:
                a[ord(s[start]) - ord('A')] -= 1
                start += 1
        return len(s) - start


