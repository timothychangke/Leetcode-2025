from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        match = 0
        k = len(s1)
        for r in range(len(s2)):
            print(c)
            if s2[r] in c:
                if not c[s2[r]]: match -= 1
                c[s2[r]] -= 1
                if not c[s2[r]]: match += 1
            if r - k >= 0 and s2[r - k] in c:
                if not c[s2[r - k]]: match -= 1
                c[s2[r - k]] += 1
                if not c[s2[r - k]]: match += 1
            if match == len(c): return True
        return False

                
        
                
                
            