class Solution:

    def encodeStr(self, s: str) -> str:
        res = ""
        for c in s:
            res = res + str(ord(c)) + "_"

        return res

    def decodeStr(self, s:str) -> str:
        ordTokens = s.split("_")[:-1]

        res = ""
        for ascii_str in ordTokens:
            if ascii_str: 
                res += chr(int(ascii_str))

        return res

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + self.encodeStr(s) + "#"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        words = s.split("#")[:-1]
        for word in words:
            decoded_word = self.decodeStr(word)
            res.append(decoded_word)

        return res
