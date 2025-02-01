from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c, l, m = Counter(s1), len(s1), 0
        for i in range(len(s2)):
            if s2[i] in c:
                if not c[s2[i]]: m -= 1
                c[s2[i]] -= 1 
                if not c[s2[i]]: m += 1
            if i >= l and s2[i - l] in c:
                if not c[s2[i - l]]: m -= 1
                c[s2[i - l]] += 1
                if not c[s2[i - l]]: m += 1
            if m == len(c):
                return True
        return False
                
