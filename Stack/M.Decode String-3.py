class Solution:
    def decodeString(self, s: str) -> str:
        cur_num = 0
        cur_str = ''
        stack = []
        for ele in s:
            if ele == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif ele == ']':
                num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + cur_str * num
            elif ele.isdigit():
                cur_num = cur_num * 10 + int(ele)
            else:
                cur_str += ele
        return cur_str