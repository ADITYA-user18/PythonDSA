nums = [3,2,3,4,3,4,4,4,4]

n = len(nums)
dict = {}

for i in range(0,len(nums)):
    if nums[i] not in dict:
        dict[nums[i]] =1
    else:
        dict[nums[i]] +=1

for key in dict:
    if dict[key] > n//2 :
        print(key)