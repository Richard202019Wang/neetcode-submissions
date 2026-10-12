class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s, map_t = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            map_s[s[i]] += 1
            map_t[t[i]] += 1
        
        return map_s == map_t
        