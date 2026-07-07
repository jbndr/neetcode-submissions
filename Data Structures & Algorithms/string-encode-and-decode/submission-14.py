class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = []
        for s in strs:
            encoding.append(s)
            encoding.append("ü")
        return "".join(encoding)

    def decode(self, s: str) -> List[str]:
        return s.split("ü")[:-1]
