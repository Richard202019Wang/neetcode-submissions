class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        result = []
        str_map = defaultdict(list)

        for s in strs:
            string_hash = [0] * 26
            for char in s:
                string_hash[ord(char) - ord('a')] += 1
            
            str_map[tuple(string_hash)].append(s)
        
        for _, vals in str_map.items():
            result.append(vals)
        
        return result
