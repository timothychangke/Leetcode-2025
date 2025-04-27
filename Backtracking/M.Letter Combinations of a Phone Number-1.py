class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1: return []
        res = []
        map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        def dfs(i, s):
            if i == len(digits): 
                res.append(s)
                return 
            for let in map[digits[i]]:
                dfs(i + 1, s + let)
        dfs(0, '')
        return res


""" 
This is a backtracking question
have a terminal condtion when i == len(s) to append the copy into res
for each letter in that number, append it to the string and call the dfs
increment i by one as well
 """
