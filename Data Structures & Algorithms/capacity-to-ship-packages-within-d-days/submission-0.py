class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 1. find out how many days for 1 weight capacity 
        # 2. then find for 2,3,4,5...
        # 2. then find out if day required, what the capacity is
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            total_days = 1
            curr_weights = 0
            for w in weights:
                if curr_weights + w <= mid:
                    curr_weights += w
                else:
                    total_days += 1
                    curr_weights = w
            if total_days > days:
                left = mid + 1
            else:
                right = mid
        return right
                

        