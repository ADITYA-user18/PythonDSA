nums = [1, 5, 7, -1, 5]
target = 6

dict= {}


for i in range(0,len(nums)):
    remain = target-nums[i]
    if remain in dict:
        print((dict[remain],nums[i]))
    else:
        dict[nums[i]] = nums[i]