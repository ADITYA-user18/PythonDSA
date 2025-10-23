def huli(arr):
    firstoccurence = {}
    max_dist=0

    for i,val in enumerate(arr):
        if val in firstoccurence:
            dist = i-firstoccurence[val]
            max_dist = max(dist,max_dist)
        else:
            firstoccurence[val] = i

    return max_dist
        
        


b = huli([1,58,455,2,4,2,5,2,532,2,2,1])
print(b)



