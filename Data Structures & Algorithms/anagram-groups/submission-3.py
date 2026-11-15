class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        word_map = defaultdict(list)
        for s in strs:
            cur = [0] * 26
            for char in s:
                cur[ord(char) - ord("a")] += 1
            
            word_map[tuple(cur)].append(s)
        
        for _, vals in word_map.items():
            result.append(vals)
        
        return result