arr = [0,1,2,3,4,6,7,8,9,10]

n =  len(arr)


expected_sum = n * (n+1) // 2
Original_sum = sum(arr)

diff = expected_sum - Original_sum
print(diff)

