nums = [100,4,200,1,3,2]

max_count = 0


for i in range(0,len(nums)):
    num = nums[i]
    count=1
    while num+1 in nums:
        count+=1
        num += 1
    max_count = max(max_count,count)

print(max_count)
