nums = [1,2,3,3,3,3,3,5,6,8,9,9,9,10,2]

count =  0

low = 0
high = len(nums)
Target=9

for num in nums:
    if num == Target:
        count+=1

print(count)


