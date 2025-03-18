class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        str = ''
        stack = []
        for c in s:
            print(stack)
            if c == '[':
                stack.append(str)
                stack.append(num)
                num = 0
                str = ''
            elif c == ']':
                prev_num = stack.pop()
                prev_str = stack.pop()
                str = prev_str + prev_num * str
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                str += c
        return str
""" 
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

num = 3
str = 'a'
stack = 3a
"""