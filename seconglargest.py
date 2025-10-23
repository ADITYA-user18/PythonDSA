arr = [1,2,3]

largest = 0

for i in range(0,len(arr)):
    first_largest = max(arr[i],largest)
for i in range(0,len(arr)):
    if arr[i]!=first_largest:
        second_largest = max(largest,arr[i])
for i in range(0,len(arr)):
    if arr[i] != second_largest  and arr[i] != first_largest:
        third_largest = max(largest,arr[i])


print(third_largest)
    


    
