
nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
target  =  3
first = -1
last = -1

for i in range(0,len(nums)):
    
    if nums[i] == target and first ==-1:
        first = i
    if nums[i]==target:
        last  = i

print(first,last)






