nums = [3,1,-2,-5,2,-4]

def AdjacentHuli(nums):
    pos = [x for x in nums if x > 0]
    neg = [x for x in nums if x < 0]

    result = []

    i,j=  0,0

    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i+=1
        j+=1

    result.extend(pos[i:])
    result.extend(neg[j:])

    return result


b =  AdjacentHuli(nums)
print(b)