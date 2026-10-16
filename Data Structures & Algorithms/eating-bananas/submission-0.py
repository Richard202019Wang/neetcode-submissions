class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_k = max(piles)
        lower_k = 1
        result = float("inf")
        while lower_k <= upper_k:
            mid = (lower_k + upper_k) // 2
            current_time = 0
            for pile in piles:
                current_time += -(-pile // mid)
            if current_time > h:
                lower_k = mid + 1
            else:
                result = mid
                upper_k = mid - 1
        return result

        