arr=[4,8,9,8,0,4,5,0,0,1,2,5,3,0,1,0]


n = len(arr)
non_zero =0


for i in range(n):
    if arr[i] != 0:
        arr[non_zero] = arr[i]
        non_zero+=1


for i in range(non_zero,n):
    arr[i] = 0 


print(arr)





