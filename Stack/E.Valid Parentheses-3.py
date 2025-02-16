class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "}": "{", "]":"["}
        stack = []
        for op in s:
            if op not in map: stack.append(op)
            elif not stack or map[op] != stack.pop():
                return False
        return not stack


