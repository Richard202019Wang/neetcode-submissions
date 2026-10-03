class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        upper_s = s.upper()
        while l < r:
            if not upper_s[l].isalnum():
                l += 1
                continue
            if not upper_s[r].isalnum():
                r -= 1
                continue
            if upper_s[l] != upper_s[r]:
                return False
            l += 1
            r -= 1

        return True
        