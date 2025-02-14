class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string = ''
        cur_num = 0
        for ele in s:
            if ele == '[':
                stack.append(cur_num)
                stack.append(cur_string)
                cur_num = 0
                cur_string = ''
            elif ele == ']':
                string = stack.pop()
                c = stack.pop()
                cur_string = string + cur_string * c
            elif ele.isdigit():
                cur_num = cur_num * 10 + int(ele)
            else:
                cur_string += ele
        return cur_string 
