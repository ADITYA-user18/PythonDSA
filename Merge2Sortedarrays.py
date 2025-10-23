def Merge2SortedArrays(arr1,arr2):

    arr1.sort()
    arr2.sort()
    res = []
    i,j = 0,0
    m,n = len(arr1),len(arr2)
    while i < m and j<n:
        if arr1[i] < arr2[j]:
            if arr1[i] not in res:
                res.append(arr1[i])
            i+=1
        elif arr2[j] < arr1[i]:
            if arr2[j] not in res:
                res.append(arr2[j])
            j+=1

        else:
            if arr1[i] not in res:
                res.append(arr1[i])
            i+=1
            j+=1
    while i < m:
        if arr1[i] not in res:
            res.append(arr1[i])
        i+=1
    while j < n:
        if arr2[j] not in res:
            res.append(arr2[j])
        j+=1
    return res
    


   
            
a = [4,2,5,7,8,6,5,4,1]
b = [8,5,48,5,65,952,8,5,6,2,1,4]

c = Merge2SortedArrays(a,b)

print(c)


        

