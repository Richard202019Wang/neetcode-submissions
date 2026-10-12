class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for st in strs:
            result += str(len(st)) + "#" + st
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        start = 0
        while start < len(s):
            current = start
            while s[current] != "#":
                current += 1
            length = int(s[start:current])
            result.append(s[current + 1 : current + 1 + length])
            start = current + 1 + length
        return result
