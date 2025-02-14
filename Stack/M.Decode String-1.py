class Solution:
    def decodeString(self, s: str) -> str:
        cur_count = 0
        cur_string = ''
        stack = []
        for c in s:
            if c == '[':
                stack.append(cur_string)
                stack.append(cur_count)
                cur_count = 0
                cur_string = ''
            elif c == ']':
                count = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + cur_string * count
            elif c.isdigit():
                cur_count = cur_count * 10 + int(c)
            else:
                cur_string += c
        return cur_string
                