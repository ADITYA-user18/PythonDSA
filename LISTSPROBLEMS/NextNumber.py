

def NextNumber(arr):
    n = len(arr)-1

    for i in range(n,-1,-1):
        if arr[i] < 9:
            arr[i] +=1
            return arr
        arr[i] = 0

    return [1] + arr

a = NextNumber([1,4,2])
print(a)
        