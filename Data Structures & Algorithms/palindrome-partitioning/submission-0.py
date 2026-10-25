class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        stack = []
        def is_palindrome(string, l , r):
            
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(j):
            if j == len(s):
                result.append(stack.copy())
                return 
            for i in range(j, len(s)):
                if is_palindrome(s, j, i):
                    stack.append(s[j : i + 1])
                    dfs(i + 1)
                    stack.pop()
        
        dfs(0)
        return result