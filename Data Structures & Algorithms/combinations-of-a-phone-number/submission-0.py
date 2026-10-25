class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digit_map = {"2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]}
        path = []

        def dfs(i):
            if i == len(digits):
                if path:
                    result.append("".join(path))
                return
            
            for dig in digit_map[digits[i]]:
                path.append(dig)
                dfs(i + 1)
                path.pop()
        dfs(0)
        return result
