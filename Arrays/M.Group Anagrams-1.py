from collections import defaultdict, Counter

def counter(str):
        alphabet = [0] * 26
        for s in str:
            pos = ord(s) - ord('a')
            alphabet[pos] += 1
        return tuple(alphabet)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for str in strs:
            map[counter(str)].append(str)
        return list(map.values())