class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq_map = defaultdict(int)
        
        hand.sort()
        for num in hand:
            freq_map[num] += 1
        
        for num in hand:
            if freq_map[num]:
                for i in range(num, num + groupSize):
                    if not freq_map[i]:
                        return False
                    freq_map[i] -= 1
        return True
        
        