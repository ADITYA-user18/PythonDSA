nums = [1,2,3]

res = [[]]

for num in nums:
    for s in res[:]:
        res.append(sorted(s+[num]))
print(res)