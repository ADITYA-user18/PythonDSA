nums = [4,5,6,7,0,1,2]



low =0
high = len(nums)-1

maxi = -float('inf')

while low<=high:
    mid = (low+high)//2

    if nums[low] <= nums[mid]:
        maxi = max(maxi,nums[mid])
        low = mid+1

    else:
        maxi = max(maxi,nums[high])
        high = mid-1
print(maxi)
