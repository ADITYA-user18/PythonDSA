
def LinearSearch(arr):
    target = 2

    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

b = LinearSearch([7,268562,66,4,78,5,4,1,4,7,52,5,6,2,5,6])

print(b)