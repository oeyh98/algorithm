class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        max_value = 0
        min_value = 100001

        for price in prices:
            if price < min_value:
                min_value = price
            elif price - min_value > result:
                result = price - min_value

        return result