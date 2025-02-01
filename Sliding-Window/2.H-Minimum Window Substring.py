from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needmap, havemap = defaultdict(int), defaultdict(int)
        for let in t:
            needmap[let] += 1
        need, have = len(needmap), 0
        l = 0
        res, resLen = [-1, -1], float('inf')
        for r in range(len(s)):
            havemap[s[r]] += 1
            if s[r] in needmap and needmap[s[r]] == havemap[s[r]]: 
                have += 1
            while have == need:
                if r - l < resLen:
                    resLen = r - l
                    res = [l, r]
                havemap[s[l]] -= 1
                if s[l] in needmap and havemap[s[l]] < needmap[s[l]]:
                    have -= 1
                l += 1
        left, right = res
        return s[left:right + 1] if resLen < float('inf') else ""
                    
                
                