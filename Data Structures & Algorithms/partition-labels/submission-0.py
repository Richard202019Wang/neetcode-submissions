class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
        
        result = []
        cur_set = set()
        cur_len = 0
        for char in s:
            char_dict[char] -= 1
            cur_set.add(char)
            if char_dict[char] == 0:
                cur_set.remove(char)
            cur_len += 1
            if not cur_set:
                result.append(cur_len)
                cur_len = 0
                continue
        return result

            