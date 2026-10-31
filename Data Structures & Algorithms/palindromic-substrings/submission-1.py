class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # def is_palindrome(l, r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True
        # result = 0

        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        dp[0][0] = True
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 2:

                        dp[i][j] = True
                        result += 1
                    elif j - i > 2 and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        result += 1
        return result
