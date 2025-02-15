class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(len(s) + ':' + s for s in strs) 

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            j = s.find(':', i)
            l = int(s[i:j])
            res.append(s[j + 1 :j + 1 + l])
            i = j + 1 + l
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))