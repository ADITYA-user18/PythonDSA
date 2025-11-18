def FloorCeil(nums,target):
    floor = -1
    ceil = -1
    low = 0
    high = len(nums)-1

    while low <= high:
     mid = (low+high)//2
     if nums[mid] == target:
        return [nums[mid],nums[mid]]
     elif nums[mid] < target:
        low = mid + 1
        floor = nums[mid]
     else:
        if nums[mid] > target:
         high = mid-1
         ceil = nums[mid]
    return [floor,ceil]


nums = [3,4,4,4,8,9,9,10,12,12,14,15]            
b = FloorCeil(nums,4)
print(b)





