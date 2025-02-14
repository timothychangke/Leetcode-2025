class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for str in strs:
            arr = [0] * 26
            for let in str: arr[ord(let) - ord('a')] +=1
            d[tuple(arr)].append(str)
        return list(d.values())