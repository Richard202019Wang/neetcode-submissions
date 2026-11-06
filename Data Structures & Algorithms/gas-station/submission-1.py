class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_tank = 0
        start_idx = 0
        total_tank = 0
        for i in range(len(gas)):
            cur_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]

            if cur_tank < 0:
                start_idx = i + 1
                cur_tank = 0
        
        return start_idx if total_tank >= 0 else -1