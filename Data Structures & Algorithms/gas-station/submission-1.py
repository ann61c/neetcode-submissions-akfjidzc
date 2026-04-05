class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        per_cost = [0] * len(gas)
        start_index = 0
        for i in range(len(gas)):
            current_tank = gas[i] - cost[i]
            per_cost[i] = current_tank
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
        if sum(per_cost) < 0:
            return -1
        for i in range(len(per_cost)):
            if per_cost[i] > 0 and i >= start_index:
                return i
        return -1

        # [1, -3, 1, -2, 3]