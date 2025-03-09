from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       ctr = list(Counter(tasks).values())
       max_f = max(ctr)
       num_of_max = ctr.count(max_f)
       return max(len(tasks), (n + 1) * (max_f - 1) + num_of_max)
