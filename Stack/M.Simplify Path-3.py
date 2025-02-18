class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        for e in path.split("/"):
            if s and e == '..':
                s.pop()
            elif e not in ['.', '', '..']: s.append(e)
        return '/' + '/'.join(s)
