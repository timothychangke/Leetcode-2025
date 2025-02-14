class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(min(len(str) for str in strs)):
            for s in strs:
                if s[i] != strs[0][i]:
                    return res
            res += s[i]
        return res