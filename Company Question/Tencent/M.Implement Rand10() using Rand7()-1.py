# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        x, y = 7, 6
        while x == 7:
            x = rand7()
        while y > 5:
            y = rand7()
        if x > 3: return y + 5
        else: return y