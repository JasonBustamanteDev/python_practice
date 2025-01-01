class Solution(object):
    def maxProfit(self, prices):
        p1 = 0
        p2 = 1
        max_profit = 0

        # Edge case: 1 or 2 length array input
        if len(prices) < 2:
            return max_profit

        while True:
            # Break condition: p2 moves beyond end of string
            if p2 > len(prices) - 1:
                break

            p1_val = prices[p1]
            p2_val = prices[p2]
            potential_profit = p2_val - p1_val

            if p2_val <= p1_val:
                p1 = p2
                p2 += 1

            else:
                max_profit = max(max_profit, potential_profit)
                p2 += 1

        return max_profit

sol = Solution().maxProfit([7,6,4,3,1])
print(sol)