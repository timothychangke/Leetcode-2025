class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if stack and a < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] > abs(a):
                        break
                    elif abs(stack[-1]) == abs(a):
                        stack.pop()
                        break
                    else:
                        stack.pop()
                else:
                    stack.append(a)
            else:
                stack.append(a)
        return stack


""" 
s = []
        for a in asteroids:
            while s and s[-1] > 0 and a < 0:
                if s[-1] + a < 0: s.pop()
                elif s[-1] + a > 0: break    
                elif s[-1] + a == 0: s.pop(); break
            else: s.append(a)
        return s
"""
