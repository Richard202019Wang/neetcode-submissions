class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            print(i)
            result += self.is_palindrome(s, i, i)
            result += self.is_palindrome(s, i, i + 1)
        return result
    def is_palindrome(self, s, l, r):
        result = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            result += 1
            l -= 1
            r += 1
        
        return result

        # dp = [[False] * len(s) for _ in range(len(s))]
        # result = 0
        # dp[0][0] = True
        
        # for i in range(len(s) - 1, -1, -1):
        #     for j in range(i, len(s)):
        #         if s[i] == s[j]:
        #             if j - i <= 2:

        #                 dp[i][j] = True
        #                 result += 1
        #             elif j - i > 2 and dp[i + 1][j - 1]:
        #                 dp[i][j] = True
        #                 result += 1
        return result
