from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in  wordList: return 0
        d = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                d[w[:i] + "*" + w[i + 1:]].append(w)
        visited = set(beginWord)
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()    
                if w == endWord: return res
                for i in range(len(w)):
                    new_w = w[:i] + '*' + w[i + 1:]
                    for nei in d[new_w]: 
                        if nei not in visited:
                            q.append(nei)
                            visited.add(w)
            res += 1
        return 0

""" 
Alternatively, you could count the difference in letters between two nodes to decide whether they are neighbours
"""