class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = float("inf")
        highest_benefit = 0
        for price in prices:
            _min = min(_min, price)
            highest_benefit = max(highest_benefit, price-_min)
        return highest_benefit