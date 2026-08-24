class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = math.ceil(sum(piles)/h)
        right = max(piles)
        while left<right:
            mid = int((left+right)/2)
            total_h = 0
            for pile in piles:
                total_h+=math.ceil(pile/mid)
            if total_h>h:
                left = mid+1
            else:
                right = mid
        return left
        