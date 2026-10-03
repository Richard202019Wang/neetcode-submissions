class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        candidates.sort()
        def dfs(i, current_sum):
            if current_sum == target:
                result.append(subset.copy())
                return

            if current_sum > target or i >= len(candidates):
                return
            subset.append(candidates[i])
            dfs(i + 1, current_sum + candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, current_sum)
        dfs(0, 0)
        return result