class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for ele in path.split('/'):
            if ele == '..':
                stack.pop()
            elif ele not in ['.', '..', '']:
                stack.append(ele)
        return "/" + "/".join(stack)
    
    """ 
    for op in operations.split("/"):
        match operation:
            case "":
                continue
            case ".":
                continue
            case "..":
                if stack: stack.pops()
            case _ :
                stack.append(op)
    return "/" if not stack else "/" + "/".join(stack)
    """