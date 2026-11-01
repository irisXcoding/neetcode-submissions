import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
                # bisearch in [1, max(piles)]
        # find a k make sum(math.ceil(pile[i]//k)>=h
        # complexity: time O(nlog(max_pail)), space: O(1)

        max_pile = max(piles)
        k = max_pile
        left, right = 1, max_pile
        while left<=right:
            mid = (left+right)//2
            if sum([math.ceil(item/mid) for item in piles])<=h:
                k = mid
                right = mid-1
            else:
                left = mid+1
        return k
