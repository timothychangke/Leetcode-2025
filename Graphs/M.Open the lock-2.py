from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: 
            return -1
        dead_set = set(deadends) 
        v = set()
        q = deque(["0000"])
        v.add("0000")
        moves = 0  
        def calcNei(combi):
            res = []
            for i in range(len(combi)):  
                for x in (-1, 1):
                    new_i = str((int(combi[i]) + x + 10) % 10)  
                    new_num = combi[:i] + new_i + combi[i + 1:]  
                    if new_num not in dead_set and new_num not in v:
                        res.append(new_num)
            return res
        while q:
            for _ in range(len(q)):
                num = q.popleft()
                if num == target:  
                    return moves  
                for nei in calcNei(num):
                    v.add(nei)  
                    q.append(nei)
            moves += 1  

        return -1
