class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = {}
        for pair in trust:
            trust_map[pair[0]] = trust_map.get(pair[0], 0) + 1
            trust_map[pair[1]] = trust_map.get(pair[1], 0) + 1
        highest = 0
        for people in trust_map:
            highest = max(highest, trust_map[people])
        print(highest)
        if highest == n - 1:
            return highest
        else:
            return -1