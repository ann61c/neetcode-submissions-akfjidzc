class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        per_cost = [0] * len(gas)
        start_index = 0
        current_tank = 0
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            per_cost[i] = current_tank
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
        return start_index
        # if sum(per_cost) < 0:
        #     return -1
        # for i in range(len(per_cost)):
        #     if per_cost[i] > 0 and i >= start_index:
        #         return i
        # print(start_index)
        # return 0

        # [2, -8, -1, 9, -1]