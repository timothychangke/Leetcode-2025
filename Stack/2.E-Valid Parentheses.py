class Solution:
    def isValid(self, s: str) -> bool:
        map = {'}': '{', ']': '[', ')': '('}
        stack = []
        for ele in s:
            if ele not in map:
                stack.append(ele)
            else:
                if not stack or stack.pop() != map[ele]:
                    return False
        return not stack