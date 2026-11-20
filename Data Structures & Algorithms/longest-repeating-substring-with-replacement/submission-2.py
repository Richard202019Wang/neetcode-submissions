class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_f, l, result = 0, 0, 0

        for r, i in enumerate(s):
            freq[i] += 1
            max_f = max(max_f, freq[i])
            while r - l + 1 - max_f > k:
                freq[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result
        