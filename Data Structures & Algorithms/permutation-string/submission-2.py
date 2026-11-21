class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1, count2 = [0] * 26, [0] * 26
        match = 0
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord("a")] += 1
            count2[ord(s2[i]) - ord("a")] += 1
        
        for i in range(len(count2)):
            if count1[i] == count2[i]:
                match += 1
        
        if match == 26:
            return True
        
        for i in range(len(s1), len(s2)):
            if match == 26:
                return True
            
            idx_in = ord(s2[i]) - ord("a")
            count2[idx_in] += 1
            if count2[idx_in] == count1[idx_in]:
                match += 1
            elif count2[idx_in] - 1 == count1[idx_in]:
                match -= 1
            
            idx_out = ord(s2[i - len(s1)]) - ord("a")
            count2[idx_out] -= 1
            if count2[idx_out] == count1[idx_out]:
                match += 1
            elif count2[idx_out] + 1 == count1[idx_out]:
                match -= 1
        
        return match == 26
        
        
        
