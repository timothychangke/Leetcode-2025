import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        lets = [[c, l] for c, l in [[-a, 'a'], [-b, 'b'], [-c, 'c']] if c < 0]
        heapq.heapify(lets)
        while lets:
            print(lets)
            count, letter = heapq.heappop(lets)
            count *= - 1
            if len(res) >= 2 and res[-2] == res[-1] == letter:
                if not lets: break
                count2, letter2 = heapq.heappop(lets)
                count2 *= -1
                res += letter2
                count2 -= 1
                if count2 > 0: heapq.heappush(lets, [-count2, letter2])
            else:
                res += letter
                count -= 1
            if count > 0: heapq.heappush(lets, [-count, letter]) 
        return res

                
        
        