class Solution:
    def isPalindrome(self, s: str) -> bool:
        return [let for let in s.lower() if let.isalnum()] == [let for let in s.lower() if let.isalnum()][::-1]