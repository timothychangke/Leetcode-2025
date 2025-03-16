from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                d[word[:i] + '*' + word[i + 1:]].append(word)
        def bfs(word):
            q = deque([word])
            v = set()
            depth = 0
            while q:
                depth += 1
                for _ in range(len(q)):
                    w = q.popleft()
                    if w == endWord: return depth
                    v.add(w)
                    for i in range(len(w)):
                        new_w = w[:i] + '*' + w[i + 1:]
                        for nw in d[new_w]:
                            if nw not in v: q.append(nw)
            return 0
        return bfs(beginWord)
        
                    
                
