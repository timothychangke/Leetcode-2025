class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d = {}
        for i, c in enumerate(s):
            d[c] = i
        seen = set()
        stack = []
        for i, c in enumerate(s):
            if c in seen: continue
            while stack and stack[-1] > c and d[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack) 
    
    
    """ 
    stack = acdb
    """           
            