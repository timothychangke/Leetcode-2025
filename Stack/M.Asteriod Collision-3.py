class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []
        # for a in asteroids:
        #     if stack and a < 0:
        #         while stack and stack[-1] > 0 and a < 0:
        #             if abs(a) > abs(stack[-1]):
        #                 stack.pop()
        #             elif abs(a) == abs(stack[-1]):
        #                 stack.pop()
        #                 break
        #             else:
        #                 break
        #         else:
        #             stack.append(a)
        #     else:
        #         stack.append(a)
        # return stack
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] == -a:
                    stack.pop()
                    break
                elif stack[-1] < -a:
                    stack.pop()
                else:
                    break 
            else:
                stack.append(a)
        return stack
                
""" 
[5,10,-15]

-1

"""