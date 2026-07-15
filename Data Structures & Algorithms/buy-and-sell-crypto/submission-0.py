class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        maxp=0

        for i in prices:
            minp=min(minp,i)
            maxp=max(maxp,i-minp)
        return maxp        