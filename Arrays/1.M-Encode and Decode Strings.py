class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for s in strs:
            res += str(len(s)) + '##' + s
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        print(s)
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j : j + 2] != '##':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 2 : j + 2 + length])
            i = j + 2 + length
        return res
       

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))