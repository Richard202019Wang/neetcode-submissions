class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        dp = [[False] * len(s) for _ in range(len(s))]

        start_idx = 0
        max_len = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        cur = j - i + 1
                        if cur > max_len:
                            max_len = cur
                            start_idx = i
        return s[start_idx : start_idx + max_len]

        