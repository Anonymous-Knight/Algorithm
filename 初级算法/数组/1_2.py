# 给定一个数组，其第i个元素的一支股票第i天的价格，计算所能获得的最大利润，交易次数不限

# 获益为售出与买入的价格之差，低价买入高价卖出；即数组中的递增序列
# 不规则序列可分解为递增序列和非递增序列，递增序列的极值差即为对应的部分利润；隐藏条件是价格大于零
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > min_price:
                profit += prices[i] - min_price
            min_price = prices[i]
        return profit
# 时间复杂度O(N)，空间复杂度O(1)

# 此题想到了贪心算法的解法，很好，简单而有效，但也应掌握通用的动态规划解法：
# 定义状态：dp[i][j]表示第i天的状态j下的现金，这里j=0表示不持股，j=1表示持股
# 状态从前往后，状态转移方程： 
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
# dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i-1])
# 定义初始状态：dp[0][0] = 0, dp[0][1] = -prices[0]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[0,0] for i in range(length)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i-1])
        return max(dp[length-1][0], dp[length-1][1] + prices[i])
# 疏漏：最后的返回值没有考虑到最后一天的操作;可考虑优化状态空间，减小空间复杂度
# 时间复杂度O(N)，空间复杂度O(N)

# 由于每一步只依赖于前一步的两个状态，可使用滚动变量将空间复杂度优化为O(1):
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        p_cash = 0  # 前一天不持股有多少钱
        p_hold = -prices[0]  # 前一天持股有多少钱
        for i in range(1, length):
            cash = max(p_cash, p_hold + prices[i-1])
            hold = max(p_hold, p_cash - prices[i-1])
            p_cash = cash
            p_hold = hold
        return max(p_cash, p_hold + prices[length - 1])
# 用变量只存储前一步状态变量，从而减小空间复杂度