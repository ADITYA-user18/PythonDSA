#  the unique elements in an array comes in the first of an array and remaining will in the rest of array
def unique(arr):
    dict={}
    for i in range(len(arr)):
        dict[arr[i]] = 0
    j=0
    for key in dict:
        arr[j] = key
        j+=1

    return arr,j


c = unique([1,1,1,2,3,4,4,7,9,9,9,8,10,6,1])
    
print(c)
    

