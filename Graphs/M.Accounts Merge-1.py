from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, x):
        res = x
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        return res
    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b: return 
        if self.rank[a] > self.rank[b]:
            self.rank[a] += self.rank[b]
            self.par[b] = a
        else:
            self.rank[b] += self.rank[a]
            self.par[a] = b
        return 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        map = {}
        uf = UnionFind(len(accounts))
        for i, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                if acc[j] in map:
                   uf.union(i, map[acc[j]]) 
                else:
                    map[acc[j]] = i
        df = defaultdict(list)
        for k, v in map.items():
            parent = uf.find(v)
            df[parent].append(k)
        res = []
        for i, emails in df.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res
        
        
            
                
                
            