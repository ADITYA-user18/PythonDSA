arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)

new_arr = [arr[n-1]]


for i in range(len(arr)-1):
    new_arr.append(arr[i])

    

print(new_arr)

