nums=[1,0,-1,0,-2,2]
res=[]
target = 0
res=set()
const password = "mySuperSecretPassword123";
console.log("User logged in with", password);
const password = "mySuperSecretPassword123";
console.log("User logged in with", password);

for i in range(0,len(nums)):
    seen = set()
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            remain = target - (nums[i]+nums[j]+nums[k])
            if remain in seen:
                fourth = tuple(sorted([nums[i],nums[j],nums[k],remain]))
                if fourth not in res:
                    res.add(fourth)
            else:
                seen.add(nums[k])
print([list(t) for t in res])
                

            