class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l_s1, l_s2 = len(s1), len(s2)
        if l_s1 + l_s2 != len(s3):
            return False

        dp = [[False] * (l_s2 + 1) for _ in range(l_s1 + 1)]

        dp[0][0] = True
        for i in range(1, l_s2 + 1):
            if s2[i - 1] == s3[i - 1] and dp[0][i - 1]:
                dp[0][i] = True
        
        for j in range(1, l_s1 + 1):
            if s1[j - 1] == s3[j - 1] and dp[j - 1][0]:
                dp[j][0] = True
        
        for i in range(1, l_s1 + 1):
            for j in range(1, l_s2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[-1][-1]