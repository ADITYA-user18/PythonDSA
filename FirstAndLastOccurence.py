
def FirstAndLastOccuranceFinder(nums,target):
    first = -1
    last = -1
    for i in range(0,len(nums)):
        if nums[i] != target:
            continue
        if nums[i] == target and first==-1:
            first=i
        if nums[i] == target:
            last=i
    return [first,last]
nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
n = FirstAndLastOccuranceFinder(nums,3)
print(n)







nums = [1,2,3,3,3,3,3,5,6,8,9,9,9,10]

