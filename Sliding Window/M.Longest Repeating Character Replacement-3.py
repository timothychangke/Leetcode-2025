class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0] * 26
        maxC, l = 0 , 0
        for r in range(len(s)):
            arr[ord(s[r]) - ord('A')] += 1
            maxC = max(arr[ord(s[r]) - ord('A')], maxC)
            if r - l + 1 - maxC > k:
                arr[ord(s[l]) - ord('A')] -= 1
                l += 1
        return len(s) - l 


""" 
s = "AABABBA", k = 1
Output: 4
window size - k = max frequency

 """
            
