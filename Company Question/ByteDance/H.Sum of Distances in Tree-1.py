class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            
        def dfs(node, parent, depth):
            ans = 1
            for nei in g[node]:
                if nei != parent:
                    ans += dfs(nei, node, depth + 1)
            weights[node] = ans
            depths[node] = depth
            return ans
        def dfs2(node, parent, w):
            res[node] = w
            for nei in g[node]:
                if nei != parent:
                    dfs2(nei, node, w - 2 * weights[nei] + n)
            
        
        weights, depths, res = [0] * n, [0] * n, [0] * n
        dfs(0, -1, 0)
        dfs2(0, -1, sum(depths))
        return res