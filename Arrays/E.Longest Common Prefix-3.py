class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]: return res
            res += shortest[i]
        return res