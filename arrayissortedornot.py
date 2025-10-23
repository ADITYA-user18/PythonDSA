def IsSorted(arr):

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False        
    return True

b = IsSorted([1,2,3,4,5,6,7])
print(b)

