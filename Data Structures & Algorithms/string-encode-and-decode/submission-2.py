class Solution:

    encode_str = ""
    decode_str = ""

    def encode(self, strs: List[str]) -> str:
        s: str = ""
        for string in strs:
            s += string + " "

        self.encode_str = s
        self.decode_str = strs

        return s

    def decode(self, s: str) -> List[str]:
        return self.decode_str
