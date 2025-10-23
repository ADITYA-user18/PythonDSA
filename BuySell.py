nums = [7,2,1,5,6,4,8]


def BuySell(nums):
    buy = nums[0]
    max_profit = 0

    for i in range(0,len(nums)):
        buy = min(buy,nums[i])
        profit = nums[i] - buy
        max_profit = max(max_profit,profit)

    return max_profit

a = BuySell(nums)
print(a)