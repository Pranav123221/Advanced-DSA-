objective 08->
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.


## Approach->
  Approach (Coin Change – Minimum Coins)
-> Use Dynamic Programming: create an array dp where dp[i] = minimum coins to make amount i
-> Initialize dp[0] = 0 and others as infinity, then for each coin update dp[i] = min(dp[i], dp[i - coin] + 1)
-> Final answer is dp[amount] (if not possible, return -1)

## constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

## code
class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1


## example:
Input: coins = [1], amount = 0
Output: 0
