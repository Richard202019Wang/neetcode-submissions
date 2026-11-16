class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        char_hash1 = [0] * 26
        char_hash2 = [0] * 26
        for i in range(len(s)):
            char_hash1[ord(s[i]) - ord('a')] += 1
            char_hash2[ord(t[i]) - ord('a')] += 1
        
        return char_hash1 == char_hash2
        