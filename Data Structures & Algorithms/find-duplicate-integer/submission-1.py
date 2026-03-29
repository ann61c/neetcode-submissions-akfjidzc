class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = set()
        for val in nums:
            if val not in res:
                res.add(val)
            else:
                return val
        return 0