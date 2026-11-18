class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_set = set()
        l, r = 0, 0
        result = 0
        if len(s) == 1:
            return 1
        while r < len(s):
            if l == r:
                cur_set.add(s[l])
                r += 1
                continue
            while l < r and s[r] in cur_set:
                cur_set.remove(s[l])
                l += 1
            
            cur_set.add(s[r])
            result = max(result, r - l + 1)
            r += 1
        
        return result
