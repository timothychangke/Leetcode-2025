from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_f = max(Counter(tasks).values())
        num_of_max_f = list(Counter(tasks).values()).count(max_f)
        return max(len(tasks), (max_f - 1) * (n + 1) + num_of_max_f)
        
        