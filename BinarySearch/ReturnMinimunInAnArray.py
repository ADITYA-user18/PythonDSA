nums = [-2,4,5,6,7,0,1,2,-1]

mini = float('inf')

low =0
high = len(nums)-1

while low<=high:
    mid = (low+high)//2

    if nums[low] <= nums[mid]:
        mini = min(mini,nums[low])
        low = mid+1
    else:
        mini = min(mini,nums[mid])
        high = mid-1
print(mini)
