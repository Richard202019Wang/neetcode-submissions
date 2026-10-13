class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        freq_list = [0] * 26
        freq_list2 = [0] * 26
        for s in s1:
            freq_list[ord(s) - ord('a')] += 1

        for i in range(len2):
            freq_list2[ord(s2[i]) - ord('a')] += 1
            if i >= len1:
                left_most = s2[i - len1]
                freq_list2[ord(left_most) - ord('a')] -= 1
            if freq_list == freq_list2:
                return True
        return False
