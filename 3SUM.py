nums = [-1, 0, 1, 2, -1, -4]
target = 0
res = set()

for i in range(0,len(nums)):
    seen = set()
    for j in range(i+1,len(nums)):
        remain = target-(nums[i]+nums[j])
        if remain in seen:
            third = tuple(sorted([nums[i],nums[j],remain]))
            if third not in res:
                res.add(third)
        else:
            seen.add(nums[j])
print([list(t) for t in res])