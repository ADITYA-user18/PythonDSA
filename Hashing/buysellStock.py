def maxprofit(prices):
    buy = prices[0]
    profit = 0

    for p in prices:
        buy = min(buy,p)
        profit = max(profit,p-buy)

    return profit,p


print(maxprofit([7,1,5,8,9,4]))