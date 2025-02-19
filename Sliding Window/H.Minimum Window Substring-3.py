from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        haveMap, needMap = defaultdict(int), defaultdict(int)
        res, resLen = [-1, -1], float('inf')
        l = 0
        for letter in t:
            needMap[letter] += 1
        have, need = 0, len(needMap)
        for r in range(len(s)):
            haveMap[s[r]] += 1
            if s[r] in needMap and haveMap[s[r]] == needMap[s[r]]:
                have += 1
            while have == need:
                if resLen > r - l + 1:
                    res = [l, r]
                    resLen = r - l + 1
                haveMap[s[l]] -= 1
                if s[l] in needMap and haveMap[s[l]] < needMap[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]: res[1] + 1] if resLen != float('inf') else ""       
                    
                
""" 

"ADOBECODEBANC"
"ABC"
needmap = {A:1, B:1, C:1}
havemap = {A:1 D:2 O:2 B:2 E:2 C:1}
need = 3, have = 3
l, r = 6, 5

have map, need map
strlen
have, need
l, r
while r:
if r in need:
havemap++
havemap[] == needmap[]
have ++
while have == need:
strlen = min(strlen, len)
res = [l, r]
l --
"""
        