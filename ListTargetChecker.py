nums = [2,4,6,7,9,77,18,19]

low =0
target =6
high = len(nums)-1

while low<=high:
    mid = (low+high)//2
    if nums[mid]==target:
        print(mid)
        break
    elif nums[mid]<target:
        low = mid+1
    else:
        if nums[mid]>target:
         high = mid-1

else:
    print('No elem')

