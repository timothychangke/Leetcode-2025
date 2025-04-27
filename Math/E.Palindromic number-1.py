class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = 0
        temp = x
        while temp > 0:
            reversed = reversed * 10 + temp % 10
            temp //= 10
        return reversed == x

""" 
obtain the reversed integer and check if they are the same
 """