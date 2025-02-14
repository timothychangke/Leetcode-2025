class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if stack and a < 0:
                while stack and stack[-1] > 0:
                    if abs(stack[-1]) < abs(a):
                        stack.pop()
                    elif abs(stack[-1]) == abs(a):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(a)
            else:
                stack.append(a)
        return stack
                    
            
        
""" 
[10, 2, -5]
-5 collides with two to form [10, -5]
-5 then collides with ten to form [10]
"""