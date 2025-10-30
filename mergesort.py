


def merge_sort(a):
    if len(a) <= 1 :
        return a
    
    mid = len(a) // 2
    left_array = merge_sort(a[:mid])
    right_array=merge_sort(a[mid:])
    return merge_array(left_array,right_array)

def merge_array(left,right):
    result = []
    i,j=0,0
    n,m = len(left),len(right)
    while i < n and j < m:
        if  left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1


    while i<n:
        result.append(left[i])
        i+=1
    while j<m:
        result.append(right[j])
        j+=1

    return result
    
    
    



a = [2,1,12,1,3,4,2,4,2,5,6,7,8,3,6,5,4]
print(merge_sort(a))

