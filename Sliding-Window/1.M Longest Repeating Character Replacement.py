class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = res = 0
        window = set()
        for r in range(len(s)):
            while 