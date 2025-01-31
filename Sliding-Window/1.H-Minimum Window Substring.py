from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needmap, window = defaultdict(int), defaultdict(int)
        res, resLen = [-1, -1], float('inf')
        for i in needmap:
            needmap[i] += 1
        need, have = len(needmap), 0
        l = 0
        for i in range(len(s)):
            window[s[i]] += 1
            if s[i] in needmap and window[s[i]] == needmap[s[i]]:
                have += 1
            while have == need:
                if i - l + 1 > resLen:
                    res = [l, i]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in needmap and needmap[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        left, right = res
        return s[left:right + 1] if resLen < float('inf') else ""






        