class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        l = len(isConnected)
        par = [i for i in range(l)]
        rank = [0] * l
        res = l
        def find(i):
            res = i
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(i, j):
            par1, par2 = find(i), find(j)
            if par1 == par2: return 0
            if rank[par1] > rank[par2]:
                rank[par1] += rank[par2]
                par[par2] = par1
            else:
                rank[par2] += rank[par1]
                par[par1] = par2
            return 1
        for i in range(l):
            for j in range(i + 1, l):  
                if isConnected[i][j] == 1:  
                    res -= union(i, j)
        
        return res