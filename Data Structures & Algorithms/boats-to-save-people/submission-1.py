class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        left = 0 
        right = len(people) - 1
        while left <= right:
            res += 1
            if people[right] + people[left] <= limit:
                left += 1
            right -=1
        return res
