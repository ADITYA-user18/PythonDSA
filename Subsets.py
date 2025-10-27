nums = [1,2,3]


res = [[]]


for num in nums:
    subsets = []
    for s in res:
        subsets.append(s+[num])
    res.extend(subsets)
print(res)


