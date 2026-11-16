class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result

    def decode(self, s: str) -> List[str]:
        num = ""
        result = []
        i = 0
        while i < len(s):

            if s[i] == "#":
                result.append(s[i + 1: i + int(num) + 1])
                i = i + int(num) + 1
                num = ""
            else:
                num += s[i]
                i += 1
            
        return result
