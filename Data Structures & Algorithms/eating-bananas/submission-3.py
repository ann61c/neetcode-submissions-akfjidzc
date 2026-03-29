class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sp = 1
        mp = max(piles)
        ans = mp

        while sp <= mp:
            mid = sp + (mp - sp)//2
            hours = 0
            for i, p in enumerate(piles):
                hours += (p + mid - 1)//mid
            print(hours)
            if hours > h:
                sp = mid + 1
            elif hours <= h:
                mp = mid - 1
                ans = mid
            
        return ans
