from collections import defaultdict
class UnionFind:
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

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accToPerson = {}
        uf = UnionFind(len(accounts))
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                if account[j] not in accToPerson:
                    accToPerson[account[j]] = i
                else:
                    uf.union(i, accToPerson[account[j]])
        personToAcc = defaultdict(list)
        for k, v in accToPerson.items():
            root = uf.find(v)
            personToAcc[root].append(k)
        res = []
        for k, v in personToAcc.items():
            res.append([accounts[k][0]] + sorted(v))
        return res
            
