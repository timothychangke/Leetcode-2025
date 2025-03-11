class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j >= len(w2): return False
                if d[w1[j]] > d[w2[j]]:
                    return False
                if d[w1[j]] < d[w2[j]]: break
        return True
        