class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        bestsell = 0
        for current in prices:
            buy = min(buy, current)
            sell = current - buy
            bestsell = max(sell, bestsell)
        return bestsell
