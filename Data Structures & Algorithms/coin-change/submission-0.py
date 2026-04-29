class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [10000000]*(amount+1)
        min_coins[0] = 0
        for i in range(amount):
            for coin in coins:
                if i + coin <= amount:
                    min_coins[i+coin] = min(min_coins[i+coin], min_coins[i]+1)
        print(min_coins)
        if min_coins[amount] == 10000000:
            return -1
        return  min_coins[amount]
