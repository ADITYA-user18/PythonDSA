nums = [17,18,20,1,3,4,5,7,8,10,11,1,3,14,16]

low = 0
high = len(nums)-1

target = 4


while low< high:
    mid = (low+high)//2

    if nums[mid]==target:
        print(mid)
        break

    if nums[low] <= nums[mid]:
        if nums[low]<=target<=nums[mid]:
            high = mid-1
        else:
            low = mid+1
    else:
        if nums[mid]<=target<=nums[high]:
            low = mid+1
        else:
            high = mid-1



        
