class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        per_cost = [0] * len(gas)
        for i in range(len(gas)):
            per_cost[i] = gas[i] - cost[i]
        if sum(per_cost) < 0:
            return -1
        for i in range(len(per_cost)):
            if per_cost[i] > 0:
                return i
        return -1