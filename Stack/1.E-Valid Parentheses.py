class Solution:
    def isValid(self, s: str) -> bool:
        map = {']': '[', '}': '{', ')': '('}
        stack = []
        for ele in s:
            if stack and ele in map:
                if stack.pop() != map[ele]: return False
            else:
                stack.append(ele)
        return True if not stack else False