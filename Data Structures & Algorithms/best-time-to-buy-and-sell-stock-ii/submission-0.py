class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # [[1,1][3,3][5,2][4,5][6,4][7,0]]



        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])

        return profit